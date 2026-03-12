class RelevanceEngine:
    def __init__(self):
        # The Hybrid Finance/Tech Matrix (0.0 to 1.0 scale)
        self.role_similarity_matrix = {
            "Quantitative Equity Analyst": {
                "Quantitative Equity Analyst": 1.0,
                "Data Scientist": 0.9,      
                "Data Analyst": 0.8,        
                "Equity Research Analyst": 0.8, 
                "Quantitative Analyst": 0.9,
                "Financial Analyst": 0.6,
                "Software Engineer": 0.5
            },
            "Data Analyst": {
                "Data Analyst": 1.0, 
                "Data Scientist": 0.7, 
                "Quantitative Equity Analyst": 0.8,
                "Software Engineer": 0.2
            }
        }

    def calculate_relevance(self, extracted_experience, target_job_title, required_years):
        """
        Calculates 'Effective' Experience by discounting irrelevant past jobs.
        """
        jobs = extracted_experience.get("experience_entries", [])
        total_effective_months = 0

        print(f"\n🎯 Target Role: {target_job_title} (Requires {required_years} years)")
        print("-" * 50)

        for job in jobs:
            past_title = job.get("job_title", "Unknown")
            duration_months = job.get("duration_months", 0)

            # Look up similarity (Default to 0.1 if completely unknown)
            similarity_score = 0.1 
            if past_title in self.role_similarity_matrix:
                similarity_score = self.role_similarity_matrix[past_title].get(target_job_title, 0.1)

            # Inject the score back into the job dictionary
            job["relevance_score"] = similarity_score

            # Math: Discount the time spent
            effective_months = duration_months * similarity_score
            total_effective_months += effective_months

            print(f"🔹 Past Role: {past_title} ({duration_months} months)")
            print(f"   Similarity to Target: {similarity_score * 100}%")
            print(f"   Effective Experience Granted: {round(effective_months, 1)} months")

        effective_years = round(total_effective_months / 12.0, 1)
        raw_years = extracted_experience.get("total_experience_years", 0.0)
        
        match_percentage = min(100, int((effective_years / required_years) * 100)) if required_years > 0 else 100

        print("-" * 50)
        return {
            "raw_total_years": raw_years,
            "effective_relevant_years": effective_years,
            "target_job": target_job_title,
            "relevance_match_percentage": match_percentage
        }