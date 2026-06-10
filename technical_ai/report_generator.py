# technical_ai/report_generator.py

class TechnicalReportGenerator:
    
    def _translate_to_english(self, param: str, score: float) -> str:
        """Translates raw mathematical scores into HR-friendly English sentences."""
        translations = {
            "accuracy": {
                1.0: "Correct and accurate answer",
                0.4: "Factually incorrect or missing key details"
            },
            "depth": {
                1.0: "Deep architectural understanding; explained trade-offs",
                0.7: "Moderate depth; explained with basic examples",
                0.4: "Surface-level or shallow answer"
            },
            "logic": {
                1.0: "Excellent step-by-step logical reasoning",
                0.7: "Good general reasoning",
                0.4: "Rushed or unstructured thought process"
            },
            "real_world": {
                1.0: "Strongly linked to production/real-world use cases",
                0.4: "Lacked practical production context"
            }
        }
        # Find the closest matching key, or return a default string
        exact_match = translations.get(param, {}).get(score)
        if exact_match:
            return exact_match
        return f"Satisfactory {param}"

    def generate_explainable_output(self, question_id: str, evaluation: dict) -> dict:
        """Fulfills Deliverable: Explainable Output Example"""
        params = evaluation["parameter_breakdown"]
        
        return {
            "question_id": question_id,
            "explanation": {
                "accuracy": self._translate_to_english("accuracy", params["accuracy"]),
                "depth": self._translate_to_english("depth", params["depth"]),
                "logic": self._translate_to_english("logic", params["logic"]),
                "real_world": self._translate_to_english("real_world", params["real_world"])
            }
        }

    def generate_final_report(self, candidate_id: str, session_history: list) -> dict:
        """
        Fulfills Deliverables: Technical Evaluation Report & Skill-Wise Breakdown.
        Takes a list of evaluated questions and compiles the master hiring document.
        """
        if not session_history:
            return {"error": "No interview data available to generate report."}

        total_score = sum(item["evaluation"]["final_normalized_score"] for item in session_history)
        avg_score = total_score / len(session_history)

        # Skill breakdown aggregation
        skills_tally = {}
        skills_count = {}
        breakdown_list = []
        strengths = set()
        weaknesses = set()

        for item in session_history:
            skill = item["skill_domain"]
            score = item["evaluation"]["final_normalized_score"]
            
            # Tally for averages
            skills_tally[skill] = skills_tally.get(skill, 0) + score
            skills_count[skill] = skills_count.get(skill, 0) + 1
            
            # Build the question-by-question breakdown
            breakdown_list.append({
                "question_id": item["question_id"],
                "skill": skill,
                "score": score,
                "depth": item["evaluation"]["depth_classification"],
                "explanation": self.generate_explainable_output(item["question_id"], item["evaluation"])["explanation"]
            })

            # Detect Strengths/Weaknesses dynamically based on normalized score
            if score >= 80:
                strengths.add(f"Strong proficiency in {skill}")
                if item["evaluation"]["depth_classification"] == "deep":
                    strengths.add("Excellent architectural and system design thinking")
            elif score < 60:
                weaknesses.add(f"Needs improvement in {skill}")
                if item["evaluation"]["parameter_breakdown"]["real_world"] == 0.4:
                    weaknesses.add("Lacks practical production experience")

        # Calculate final skill averages
        final_skills = {skill: round(skills_tally[skill] / skills_count[skill], 1) for skill in skills_tally}

        # Make the final hiring decision based on Phase 7 rules
        decision = "Strong Technical Fit" if avg_score >= 75 else "Needs Growth / Junior Role"

        return {
            "candidate_id": candidate_id,
            "overall_technical_score": round(avg_score, 1),
            "decision": decision,
            "skills_breakdown": final_skills,
            "strengths": list(strengths)[:3],  # Cap at top 3 for readability
            "weaknesses": list(weaknesses)[:3],
            "detailed_question_breakdown": breakdown_list
        }