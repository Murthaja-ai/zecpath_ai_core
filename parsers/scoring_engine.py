import json
import os

class ScoringEngine:
    def __init__(self):
        print("⚖️ Booting up Dynamic Scoring Engine...")
        # Automatically find and load the scoring_weights.json file
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "data", "scoring_weights.json")
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Could not find config file at {config_path}")
            
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = json.load(f)

    def calculate_final_score(self, role_level, scores):
        """
        Takes raw scores, applies dynamic weights based on role, 
        handles missing data, and returns an audit trail.
        """
        # 1. Validate the role level
        if role_level not in self.config["roles"]:
            raise ValueError(f"Invalid role_level '{role_level}'. Must be: {list(self.config['roles'].keys())}")
        
        # 2. Get the base weights for this specific role
        weights = self.config["roles"][role_level]["weights"].copy()
        
        audit_notes = []
        
        # 3. MISSING DATA HANDLER: The Fallback Rule
        # If the parser couldn't find an Education section, we don't punish the candidate with a 0%.
        # We trigger the fallback rule: Distribute education weight to Skills and Experience.
        if scores.get("education") is None:
            audit_notes.append("⚠️ Missing Education Data. Redistributing weight evenly to Skills and Experience.")
            missing_weight = weights["education"]
            
            weights["skills"] += (missing_weight / 2)
            weights["experience"] += (missing_weight / 2)
            weights["education"] = 0.0  # Turn off education weighting
            
            scores["education"] = 0.0   # Default to 0 so the math doesn't break
        
        # Ensure other fields aren't completely missing
        for key in ["skills", "experience", "projects"]:
            if scores.get(key) is None:
                scores[key] = 0.0
                audit_notes.append(f"⚠️ Missing {key.capitalize()} Data. Defaulting to 0.0.")

        # 4. CALCULATE THE FINAL WEIGHTED SCORE
        final_score = (
            (scores["skills"] * weights["skills"]) +
            (scores["experience"] * weights["experience"]) +
            (scores["projects"] * weights["projects"]) +
            (scores["education"] * weights["education"])
        )
        
        # 5. GENERATE THE AUDIT TRAIL (The Legal Receipt)
        return {
            "role_level": role_level,
            "final_score": round(final_score, 3),
            "effective_weights": weights,
            "raw_scores": scores,
            "audit_notes": audit_notes
        }