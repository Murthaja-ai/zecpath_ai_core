class IntegrityChecker:
    def __init__(self):
        print("🕵️ Booting up Anti-Cheat System (Integrity & Bias Checker)...")

    def analyze_resume_integrity(self, resume_text, extracted_skills):
        """
        Checks for 'Keyword Stuffing' by calculating the density of skills 
        compared to the total length of the resume.
        """
        # 1. Count total words in the resume
        total_words = len(resume_text.split())
        if total_words == 0:
            return {"status": "FLAGGED", "reason": "Resume contains no readable text."}

        # 2. Count how many skills were extracted
        total_skills = len(extracted_skills)

        # 3. Calculate Density Ratio (Skills per 100 words)
        # Normal resumes usually have about 5 to 10 skills per 100 words.
        density_ratio = (total_skills / total_words) * 100

        # 4. Apply Governance Rules
        if density_ratio > 15.0:
            return {
                "status": "FLAGGED",
                "reason": f"Abnormal Skill Density ({density_ratio:.1f}%). Possible Keyword Stuffing detected.",
                "penalty": 0.50 # Cut their final score in half
            }
        elif total_words > 3000:
            return {
                "status": "FLAGGED",
                "reason": "Resume exceeds standard length. Possible hidden text detected.",
                "penalty": 0.20 # 20% penalty
            }
        else:
            return {
                "status": "CLEAN",
                "reason": "Standard text patterns detected.",
                "penalty": 0.0
            }