# advanced_features_v2/concept_ai_coach.py

class NextGenAICoach:
    @staticmethod
    def generate_mentorship_prompt(candidate_id: str, scores: dict, final_decision: str) -> str:
        """
        V2.0 Proof of Concept:
        Instead of just printing "Rejected", this constructs a dynamic LLM prompt 
        based on the Day 54 Variance Engine data, turning the ATS into a mentor.
        """
        base_prompt = f"You are an empathetic Senior Tech Recruiter at Zecpath. Write a personalized feedback email to Candidate {candidate_id}.\n"
        
        if final_decision.upper() == "REJECTED":
            base_prompt += "The candidate was unfortunately rejected. Soften the blow, but provide actionable feedback based on these metrics:\n"
            
            # Leveraging our Day 54 Variance Logic
            tech_score = scores.get('technical', 0)
            hr_score = scores.get('hr', 0)
            
            if tech_score > 85 and hr_score < 60:
                base_prompt += f"- Highlight: They are clearly a brilliant coder (Technical: {tech_score}%).\n"
                base_prompt += f"- Area for Growth: Their soft skills and communication need work (HR: {hr_score}%). Suggest practicing behavioral interviews.\n"
            elif tech_score < 60:
                base_prompt += "- Area for Growth: Suggest foundational courses in system architecture and coding assessments.\n"
                
        elif final_decision.upper() == "HOLD / REVIEW":
            base_prompt += "The candidate has been placed on hold for a human review. Congratulate them on passing the technical bar and explain next steps.\n"

        base_prompt += "\nTone constraint: Professional, warm, and highly constructive. Do not sound like a robot."
        return base_prompt

if __name__ == "__main__":
    # Simulating our "Volatile Genius" from Day 56
    demo_scores = {"ats": 90.0, "screening": 60.0, "hr": 40.0, "technical": 99.0}
    
    print("="*60)
    print("🧠 V2.0 AI COACH PROMPT GENERATOR (PROOF OF CONCEPT)")
    print("="*60 + "\n")
    
    generated_prompt = NextGenAICoach.generate_mentorship_prompt("P_003_GENIUS", demo_scores, "REJECTED")
    print(generated_prompt)
    print("\n" + "="*60)