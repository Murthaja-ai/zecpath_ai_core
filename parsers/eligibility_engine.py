import os
import json

class EligibilityEngine:
    def __init__(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.rules_path = os.path.join(base_dir, "data", "demo_dataset", "eligibility_rules.json")
        self.rules = self._load_rules()

    def _load_rules(self):
        try:
            with open(self.rules_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"⚠️ Could not load eligibility rules: {e}")
            return {}

    def safe_value(self, value, default):
        """Edge Case Handling from Company Spec"""
        return value if value is not None else default

    def evaluate_candidate(self, candidate_data, ats_score, role_name):
        """Evaluates candidate and returns Company Spec JSON structure"""
        job_rules = self.rules.get(role_name, {})
        
        # 1. Extract Candidate Data safely
        candidate_id = self.safe_value(candidate_data.get("filename"), "Unknown")
        candidate_skills = [s.lower() for s in self.safe_value(candidate_data.get("skills", []), [])]
        candidate_exp = self.safe_value(candidate_data.get("experience_years"), 0)
        candidate_loc = self.safe_value(candidate_data.get("location", ""), "").lower()
        candidate_avail = self.safe_value(candidate_data.get("available", True), True)

        # 2. Extract Rules safely (with defaults)
        min_ats_score = job_rules.get("min_ats_score", 70)
        mandatory_skills = [s.lower() for s in job_rules.get("mandatory_skills", [])]
        min_exp = job_rules.get("experience", {}).get("min_years", 0)
        max_exp = job_rules.get("experience", {}).get("max_years", 10)
        allowed_locations = [loc.lower() for loc in job_rules.get("allowed_locations", [])]
        req_availability = job_rules.get("availability_required", False)

        # 3. Perform Checks
        skill_ok = all(skill in candidate_skills for skill in mandatory_skills) if mandatory_skills else True
        exp_ok = min_exp <= candidate_exp <= max_exp
        loc_ok = (candidate_loc in allowed_locations) if allowed_locations else True
        avail_ok = candidate_avail if req_availability else True

        # 4. Company Decision Logic
        if ats_score >= min_ats_score and skill_ok and exp_ok and loc_ok and avail_ok:
            status = "Eligible"
        elif ats_score >= (min_ats_score - 15):
            status = "Review"
        else:
            status = "Rejected"

        # 5. Return exact expected structure
        return {
            "candidate_id": candidate_id,
            "eligibility_status": status,
            "checks": {
                "ats_score": ats_score,
                "skill_match": skill_ok,
                "experience_match": exp_ok,
                "location_match": loc_ok,
                "availability_match": avail_ok
            }
        }