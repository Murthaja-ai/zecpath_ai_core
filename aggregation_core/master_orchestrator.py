# aggregation_core/master_orchestrator.py
from calculation_engine import AggregationMathEngine

class CrossRoundOrchestrator:
    def __init__(self):
        self.math_engine = AggregationMathEngine()

    def _determine_hr_fit(self, final_percentage: float) -> dict:
        """Fixes the baseline contradiction by unifying Fit and Decision boundaries."""
        if final_percentage >= 85:
            return {"fit_category": "Excellent Fit", "decision": "Hire"}
        elif final_percentage >= 70:
            return {"fit_category": "Strong Fit", "decision": "Hire"}
        elif final_percentage >= 55:
            return {"fit_category": "Moderate Fit", "decision": "Consider"}
        else:
            return {"fit_category": "Low Fit", "decision": "Reject"}

    def _generate_explainable_ai_text(self, normalized_scores: dict, hr_fit: dict) -> str:
        """Generates dynamic explanation text rather than static hardcoded strings."""
        if not normalized_scores:
            return "Insufficient data to generate evaluation."

        # Find strongest and weakest rounds dynamically
        strongest_round = max(normalized_scores, key=normalized_scores.get)
        weakest_round = min(normalized_scores, key=normalized_scores.get)

        strong_val = normalized_scores[strongest_round]
        weak_val = normalized_scores[weakest_round]

        explanation = (f"Candidate resulted in a {hr_fit['fit_category']} ({hr_fit['decision']}). "
                       f"Their strongest indicator was the {strongest_round} phase ({strong_val}%), ")

        if weak_val < 60:
            explanation += f"though performance dropped during the {weakest_round} phase ({weak_val}%), which dragged their overall average down."
        else:
            explanation += f"and they maintained solid consistency, with their lowest phase ({weakest_round}) still yielding a competent {weak_val}%."

        return explanation

    def process_candidate_profile(self, candidate_id: str, role_type: str, raw_scores: dict) -> dict:
        """The master pipeline that generates the final API payload."""
        
        # 1. Run the Math Engine (Handles missing rounds + normalization)
        calculation_results = self.math_engine.calculate_unified_score(role_type, raw_scores)
        
        final_score = calculation_results.get("final_percentage", 0.0)
        norm_scores = calculation_results.get("normalized_raw_scores", {})
        
        # 2. Determine Business Logic (HR Fit)
        hr_fit = self._determine_hr_fit(final_score)

        # 3. Generate Explainable AI (XAI)
        explanation_text = self._generate_explainable_ai_text(norm_scores, hr_fit)

        # 4. Construct Final Enterprise Payload
        return {
            "candidate_id": candidate_id,
            "role_evaluated": role_type,
            "unified_score": final_score,
            "hr_recommendation": hr_fit,
            "explainable_ai_summary": explanation_text,
            "telemetry": {
                "missing_data_reweighted": calculation_results["missing_rounds_handled"],
                "applied_dynamic_weights": calculation_results["dynamically_applied_weights"],
                "cohort_normalized_scores": norm_scores
            }
        }