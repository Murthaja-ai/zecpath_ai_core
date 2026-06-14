# recommendation_core/engine_brain.py
import json
import os

class DecisionBrain:
    def __init__(self):
        """Loads the strict corporate compliance rules."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, 'decision_rules.json')
        
        with open(config_path, 'r') as f:
            self.rules = json.load(f)

    def _apply_risk_penalties(self, base_score: float, behavior_risk: str, integrity_risk: str) -> float:
        """Applies soft numeric penalties for moderate risks."""
        penalties = self.rules["risk_penalties"]
        
        b_penalty = penalties["behavior_risk"].get(behavior_risk, 0)
        i_penalty = penalties["integrity_risk"].get(integrity_risk, 0)
        
        adjusted_score = max(base_score - (b_penalty + i_penalty), 0)
        return round(adjusted_score, 2)

    def _calculate_confidence_index(self, phase_scores: dict, risks: dict) -> float:
        """
        Fixes the variance bug. Confidence is now based on:
        1. Number of completed rounds (Data completeness).
        2. Presence of erratic risk flags.
        """
        if not phase_scores:
            return 0.0
            
        base_confidence = 100.0
        
        # 1. Penalty for missing data (e.g., didn't take machine test)
        expected_rounds = 5
        actual_rounds = len([v for v in phase_scores.values() if v is not None])
        missing_penalty = ((expected_rounds - actual_rounds) / expected_rounds) * 40
        base_confidence -= missing_penalty
        
        # 2. Volatility penalty for high risks
        if risks.get("behavior") == "High Risk" or risks.get("integrity") == "High Risk":
            base_confidence -= 15 # AI is less confident recommending risky profiles
            
        return max(round(base_confidence, 2), 10.0)

    def evaluate_candidate(self, unified_score: float, phase_scores: dict, behavior_risk: str, integrity_risk: str) -> dict:
        """The master evaluation flow."""
        
        # 1. Check Hard Gates First (The CEO Override)
        gates = self.rules["compliance_hard_gates"]
        if integrity_risk == gates["integrity_override"]["trigger_status"]:
            return {
                "decision": gates["integrity_override"]["forced_decision"],
                "adjusted_score": 0.0, # Nullify score
                "confidence_score": 99.0, # Very confident in rejecting a cheater
                "override_triggered": True,
                "override_reason": gates["integrity_override"]["rationale"]
            }
            
        if behavior_risk == gates["behavior_override"]["trigger_status"]:
            return {
                "decision": gates["behavior_override"]["forced_decision"],
                "adjusted_score": unified_score, 
                "confidence_score": 85.0,
                "override_triggered": True,
                "override_reason": gates["behavior_override"]["rationale"]
            }

        # 2. Apply Standard Math if no Hard Gates were triggered
        adjusted_score = self._apply_risk_penalties(unified_score, behavior_risk, integrity_risk)
        
        thresholds = self.rules["score_thresholds"]
        if adjusted_score >= thresholds["selected"]:
            decision = "Selected"
        elif adjusted_score >= thresholds["hold_review"]:
            decision = "Hold / Review"
        else:
            decision = "Rejected"
            
        confidence = self._calculate_confidence_index(phase_scores, {"behavior": behavior_risk, "integrity": integrity_risk})

        return {
            "decision": decision,
            "adjusted_score": adjusted_score,
            "confidence_score": confidence,
            "override_triggered": False,
            "override_reason": None
        }