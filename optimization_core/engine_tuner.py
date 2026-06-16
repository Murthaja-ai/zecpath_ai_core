# optimization_core/engine_tuner.py

class OptimizedDecisionEngine:
    def __init__(self, select_threshold: float = 78.0, hold_threshold: float = 58.0):
        # We lowered the selection threshold slightly from 80 to 78 to improve candidate recall 
        # (reducing False Negatives where great candidates were barely missing the cutoff).
        self.thresholds = {
            "SELECTED": select_threshold,
            "HOLD_REVIEW": hold_threshold
        }

    def evaluate_candidate_edge_cases(self, refined_score: float, technical_score: float, integrity_status: str) -> str:
        """
        Optimizes edge cases using decoupled rule-checking patterns.
        """
        # 1. FALSE POSITIVE PREVENTION (The Hard Gate)
        # Never allow a high score to override a severe compliance/integrity breach.
        if integrity_status.strip().title() == "High Risk":
            return "Rejected"

        # 2. FALSE NEGATIVE PREVENTION (The Talent Saver)
        # Protect highly technical talent whose aggregate score dipped due to weak soft-skills.
        if refined_score < self.thresholds["HOLD_REVIEW"] and technical_score >= 85.0:
            return "Hold / Review"

        # 3. STANDARD OPTIMIZED BOUNDARIES
        if refined_score >= self.thresholds["SELECTED"]:
            return "Selected"
        elif refined_score >= self.thresholds["HOLD_REVIEW"]:
            return "Hold / Review"
            
        return "Rejected"