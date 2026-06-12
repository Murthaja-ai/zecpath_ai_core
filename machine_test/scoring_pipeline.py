# machine_test/scoring_pipeline.py
from evaluation_engine import MachineTestEngine

class PracticalScoringPipeline:
    def __init__(self):
        self.engine = MachineTestEngine()

    def process_machine_test(self, task_type: str, execution_data: dict, candidate_code: str, integrity_data: dict) -> dict:
        """
        The master orchestrator. Evaluates practical coding skills AND 
        enforces the Phase 9 Integrity Shield.
        """
        # 1. Get the raw technical evaluation
        technical_result = self.engine.evaluate_submission(task_type, execution_data, candidate_code)
        final_score = technical_result["task_score"]
        
        # 2. Phase 9 Cross-Module Integration: The Integrity Interlock
        integrity_score = integrity_data.get("integrity_score", 100)
        is_breach = integrity_data.get("risk_level", "").startswith("High Risk") or integrity_score < 50
        
        # 3. Determine HR Decision based on score (and cheating status)
        if is_breach:
            decision = "Disqualified: Integrity Compromise"
            hr_flag = "CRITICAL: Candidate flagged for malpractice during practical test."
            final_score = 0.0 # Nullify their score
        elif final_score >= 85:
            decision = "Excellent Match"
            hr_flag = "Candidate demonstrated senior-level practical execution."
        elif final_score >= 70:
            decision = "Competent Practitioner"
            hr_flag = "Solid fundamental skills, acceptable for mid-level roles."
        else:
            decision = "Needs Review"
            hr_flag = "Practical execution fell below acceptable enterprise standards."

        # 4. Construct the Final Payload for the ATS/Dashboard
        return {
            "evaluation_module": "Phase 10 - Machine Test",
            "task_context": technical_result["applied_schema"],
            "final_practical_score": final_score,
            "sub_metric_breakdown": technical_result["sub_metrics"],
            "integrity_validation": {
                "score_received": integrity_score,
                "breach_detected": is_breach
            },
            "hr_decision": decision,
            "recruiter_notes": hr_flag
        }