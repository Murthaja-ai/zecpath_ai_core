# integrity_ai/integrity_engine.py
import json
import os

class IntegrityEngine:
    def __init__(self):
        """Initializes the security shield and pulls rules from the schema configuration."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(base_dir, 'integrity_schema.json')
        
        with open(schema_path, 'r') as f:
            self.rules = json.load(f)

    def assess_interview_integrity(self, events: dict, context: str = "conceptual_probing") -> dict:
        """
        Analyzes live security telemetry against dynamic, context-aware rule sets.
        
        Input events schema:
        {
            "tab_switch": int,
            "focus_loss": int,
            "voice_detect": int,
            "gaze_off": int
        }
        """
        # 1. Gracefully resolve context rules to prevent clashing with Phase 8
        context_rules = self.rules["context_threshold_overrides"].get(context)
        if not context_rules:
            raise ValueError(f"Security Engine Error: Active context state '{context}' is invalid.")

        # 2. Extract baseline counts
        tab_switch = events.get("tab_switch", 0)
        focus_loss = events.get("focus_loss", 0)
        voice_detect = events.get("voice_detect", 0)
        gaze_off = events.get("gaze_off", 0)

        # 3. Apply Base Deductions
        base_score = 100
        base_score -= (tab_switch * 6)
        base_score -= (focus_loss * 4)
        base_score -= (voice_detect * 12)
        base_score -= (gaze_off * 3)

        # 4. Process Compounding Multi-Signal Violations (Heuristics)
        compounding_penalty = 0
        if gaze_off > 0 and voice_detect > 0:
            # Candidate is looking away *while* a voice is talking
            compounding_penalty += 15
        if tab_switch > 0 and focus_loss > 0:
            # Candidate switched tabs and minimized our browser window
            compounding_penalty += 10

        final_score = max(0, base_score - compounding_penalty)

        # 5. Evaluate Flags against Context-Specific Tolerances
        active_flags = []
        realtime_warnings = []

        if tab_switch > context_rules["tab_switch_limit"]:
            active_flags.append("EXCESSIVE_TAB_SWITCHING")
            realtime_warnings.append("Security Alert: Please keep your application focus within the core interview window.")
            
        if voice_detect > context_rules["voice_detect_limit"]:
            active_flags.append("UNAUTHORIZED_VOICE_DETECTION")
            realtime_warnings.append("Audio Warning: Secondary voice signature isolated. Ensure your workspace remains silent.")

        if gaze_off > context_rules["gaze_off_limit"]:
            active_flags.append("SUSPICIOUS_GAZE_PATTERN")
            realtime_warnings.append("Focus Alert: Continuous peripheral gaze detected. Please view the interface directly.")

        # 6. Establish Global Risk Tagging
        if final_score < 50 or "EXCESSIVE_TAB_SWITCHING" in active_flags:
            risk_level = "High Risk / Flagged System Breach"
        elif final_score < 75:
            risk_level = "Moderate Risk / Anomalous Pattern"
        else:
            risk_level = "Low Risk / Fully Verified Integrity"

        return {
            "integrity_score": final_score,
            "risk_level": risk_level,
            "triggered_flags": active_flags,
            "realtime_candidate_warnings": realtime_warnings,
            "context_shield_applied": context
        }

    def unify_with_behavior(self, behavior_score: float, integrity_score: float) -> float:
        """Balances behavioral tracking data safely against technical security indicators."""
        # Integrity score holds structural precedence (60% weight) to maintain system safety
        unified_metric = (behavior_score * 0.40) + (integrity_score * 0.60)
        return round(unified_metric, 2)