from sentence_transformers import SentenceTransformer, util
from functools import lru_cache  # <-- NEW: Import the memory cache tool

class SemanticEngine:
    def __init__(self):
        print("🧠 Loading AI Embedding Model (This takes a few seconds)...")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        # We set a threshold: If semantic distance is > 0.50, we consider it a match
        self.threshold = 0.50 

    # --- THE ENTERPRISE UPGRADE ---
    @lru_cache(maxsize=10000)
    def get_embedding(self, text):
        """
        Calculates the AI vector once, then memorizes it. 
        maxsize=10000 means it can memorize up to 10,000 unique skills/words.
        """
        return self.model.encode(text, convert_to_tensor=True)

    def calculate_similarity(self, text1, text2):
        if not text1 or not text2:
            return 0.0
        
        # <-- CHANGED: Now we ask the memory cache instead of the heavy model directly!
        embedding1 = self.get_embedding(text1)
        embedding2 = self.get_embedding(text2)
        
        return round(util.cos_sim(embedding1, embedding2).item(), 3)
        
    def analyze_skill_gap(self, candidate_skills, jd_skills):
        """Performs a semantic skill gap analysis (Matched vs Missing)."""
        if not jd_skills:
            return {"score": 0.0, "matched": [], "missing": []}
            
        matched_skills = []
        missing_skills = []
        total_score = 0.0
        
        for jd_skill in jd_skills:
            if not candidate_skills:
                missing_skills.append(jd_skill)
                continue
                
            # Find the closest semantic match in the candidate's list
            best_match_score = max([self.calculate_similarity(jd_skill, c_skill) for c_skill in candidate_skills])
            
            # If the score is higher than our threshold, it's a match!
            if best_match_score >= self.threshold:
                matched_skills.append(jd_skill)
                total_score += best_match_score
            else:
                missing_skills.append(jd_skill)
                total_score += best_match_score # We still keep partial credit for the score
                
        avg_score = round(total_score / len(jd_skills), 3)
        
        return {
            "score": avg_score,
            "matched": matched_skills,
            "missing": missing_skills
        }