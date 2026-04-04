import json
import os
import csv # <-- Added for CSV Export

class RankingEngine:
    def __init__(self):
        print("🏆 Booting up the Candidate Ranking & Shortlisting Engine (V2 - Enterprise Export)...")
        
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "data", "shortlist_rules.json")
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Could not find config file at {config_path}")
            
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def rank_and_filter(self, candidates):
        """Sorts, applies thresholds, and generates recruiter notes."""
        sorted_candidates = sorted(
            candidates,
            key=lambda c: (
                c.get("final_score", 0),
                c.get("raw_scores", {}).get("skills", 0),
                c.get("raw_scores", {}).get("experience", 0)
            ),
            reverse=True
        )

        thresholds = self.config["thresholds"]
        max_shortlist = self.config["ranking_config"]["max_shortlist_size"]
        total_candidates = len(sorted_candidates)
        
        shortlist_count = 0
        processed_results = []

        for index, candidate in enumerate(sorted_candidates):
            score = candidate.get("final_score", 0) * 100 
            
            # --- STATUS ASSIGNMENT ---
            if score >= thresholds["auto_shortlist"]["min_score"]:
                if shortlist_count < max_shortlist:
                    status_info = thresholds["auto_shortlist"].copy()
                    shortlist_count += 1
                else:
                    status_info = thresholds["manual_review"].copy()
                    status_info["recommended_action"] = "Shortlist Full. Keep as Backup."
            elif score >= thresholds["manual_review"]["min_score"]:
                status_info = thresholds["manual_review"].copy()
            else:
                status_info = thresholds["auto_reject"].copy()

            # --- GENERATE RECRUITER NOTE (Stolen from Friend 1) ---
            # Creates a plain-english summary for HR
            skill_score = candidate.get("raw_scores", {}).get("skills", 0) * 100
            exp_score = candidate.get("raw_scores", {}).get("experience", 0) * 100
            recruiter_note = f"{status_info['status_label']} due to {score:.1f}% total match. (Skills: {skill_score:.0f}%, Exp: {exp_score:.0f}%)"

            # --- ATTACH METADATA ---
            candidate["ats_rank"] = index + 1
            candidate["ats_percentile"] = round(((total_candidates - (index + 1)) / total_candidates) * 100, 1) # Stolen from Friend 2
            candidate["ats_status"] = status_info["status_label"]
            candidate["ats_action"] = status_info["recommended_action"]
            candidate["final_percentage"] = round(score, 1)
            candidate["recruiter_note"] = recruiter_note

            processed_results.append(candidate)

        return processed_results

    def export_to_csv(self, processed_candidates, output_filename="hr_shortlist_report.csv"):
        """Exports the ranked list to a recruiter-friendly CSV file (Stolen from Friend 3)."""
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        output_dir = os.path.join(base_dir, "data", "processed")
        os.makedirs(output_dir, exist_ok=True)
        
        filepath = os.path.join(output_dir, output_filename)
        
        # Define the exact columns HR wants to see
        headers = ["ats_rank", "ats_percentile", "candidate_name", "final_percentage", "ats_status", "ats_action", "recruiter_note"]
        
        with open(filepath, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for c in processed_candidates:
                # Only write the specific headers to the CSV, not the raw code data
                row = {h: c.get(h, "") for h in headers}
                writer.writerow(row)
                
        print(f"✅ SUCCESS: HR Report exported to {filepath}")
        return filepath