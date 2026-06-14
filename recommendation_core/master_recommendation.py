# recommendation_core/master_recommendation.py
from engine_brain import DecisionBrain

class FinalRecommendationOrchestrator:
    def __init__(self):
        self.brain = DecisionBrain()

    def _generate_narrative(self, raw_score: float, evaluation: dict, risks: dict) -> dict:
        """Translates the AI's internal logic into a plain-English explanation."""
        decision = evaluation["decision"]
        
        strengths = []
        weaknesses = []
        
        if raw_score >= 80: strengths.append("Strong technical/aggregate foundation.")
        if risks["behavior"] == "Low Risk": strengths.append("Excellent behavioral alignment.")
        
        if risks["behavior"] != "Low Risk": weaknesses.append(f"Behavioral Flag: {risks['behavior']}.")
        if risks["integrity"] != "Low Risk": weaknesses.append(f"Integrity Flag: {risks['integrity']}.")

        # Narrative Generation
        if evaluation["override_triggered"]:
            rationale = f"HARD GATE ENFORCED: {evaluation['override_reason']}"
        elif decision == "Selected":
            rationale = f"Candidate achieved a strong adjusted score of {evaluation['adjusted_score']}% with acceptable risk margins. Recommended for immediate offer."
        elif decision == "Hold / Review":
            rationale = f"Candidate scored {evaluation['adjusted_score']}%. Proceed with caution; manual HR review advised due to moderate scores or risk penalties."
        else:
            rationale = f"Candidate adjusted score ({evaluation['adjusted_score']}%) falls below acceptable enterprise thresholds."

        return {
            "rationale_narrative": rationale,
            "identified_strengths": strengths,
            "identified_weaknesses": weaknesses
        }

    def process_final_decision(self, candidate_id: str, unified_score: float, phase_scores: dict, behavior_risk: str, integrity_risk: str) -> dict:
        """Generates the absolute final API payload for Zecpath."""
        
        # 1. Run the Brain
        evaluation = self.brain.evaluate_candidate(unified_score, phase_scores, behavior_risk, integrity_risk)
        
        # 2. Generate Explainable Narrative
        explanation = self._generate_narrative(unified_score, evaluation, {"behavior": behavior_risk, "integrity": integrity_risk})
        
        # 3. Output Final Payload
        return {
            "candidate_id": candidate_id,
            "final_recommendation": evaluation["decision"],
            "ai_confidence_index": evaluation["confidence_score"],
            "scoring_telemetry": {
                "raw_unified_score": unified_score,
                "risk_adjusted_score": evaluation["adjusted_score"],
            },
            "risk_profile": {
                "behavioral_status": behavior_risk,
                "integrity_status": integrity_risk
            },
            "automated_explanation": explanation
        }