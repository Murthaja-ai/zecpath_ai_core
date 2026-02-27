import json
import os
import re

class SkillExtractor:
    def __init__(self):
        # 1. Load the Skill Database
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "..", "data", "skills_db.json")
        
        try:
            with open(db_path, "r", encoding="utf-8") as f:
                self.skill_db = json.load(f)
            print(f"✅ Loaded {len(self.skill_db)} skills from database.")
        except FileNotFoundError:
            print("❌ Error: skills_db.json not found. Please create it in 'data' folder.")
            self.skill_db = []

    def extract_skills(self, text):
        """
        Scans text for skills and returns a dictionary with confidence scores.
        Output format: {'Python': 100, 'Machine Learning': 90, 'NumPy': 50}
        """
        found_skills = {} # Dictionary to store Skill + Score
        text_lower = text.lower()

        # 2. Direct Extraction Loop
        for skill in self.skill_db:
            official_name = skill["name"]
            score = 0
            
            # Check A: Exact Match (High Confidence)
            if self._is_match(official_name, text_lower):
                score = 100 
            
            # Check B: Alias Match (Medium Confidence)
            else:
                for alias in skill.get("aliases", []):
                    if self._is_match(alias, text_lower):
                        score = 90
                        break # Stop checking aliases if one matches
            
            # If we found the skill, save it!
            if score > 0:
                # Only update if we found a higher score (e.g., don't downgrade 100 to 90)
                if found_skills.get(official_name, 0) < score:
                    found_skills[official_name] = score

                # --- NEW: SKILL STACK INFERENCE (The "Magic" Part) ---
                # If they know "Pandas", they probably know "NumPy" too.
                # We add these as "Inferred Skills" with Low Confidence (50%).
                for related in skill.get("related_skills", []):
                    # Only add if we haven't found this skill explicitly yet
                    if related not in found_skills:
                        found_skills[related] = 50 

        return found_skills

    def _is_match(self, keyword, text):
        """
        Helper: Returns True if the keyword exists as a whole word.
        """
        # \b ensures we match "Java" but not "JavaScript" by accident
        pattern = r'\b' + re.escape(keyword.lower()) + r'\b'
        return re.search(pattern, text) is not None

# --- Test Block ---
if __name__ == "__main__":
    extractor = SkillExtractor()
    
    # Test Text: Mentions "Pandas" (Official) and "ML" (Alias)
    # It does NOT mention "NumPy", but our logic should guess it!
    sample_text = """
    I am a Data Scientist. I use Pandas for data cleaning and ML for prediction.
    """
    
    print("\n🔍 Scanning Sample Text...")
    skills = extractor.extract_skills(sample_text)
    
    print("\n--- 📊 Final Skill Report ---")
    for skill, confidence in skills.items():
        print(f"🔹 {skill}: {confidence}% Confidence")