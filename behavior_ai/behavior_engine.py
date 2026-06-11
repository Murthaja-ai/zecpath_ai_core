# behavior_ai/behavior_engine.py
import json
import os

class BehavioralEngine:
    def __init__(self):
        """Initializes the engine and dynamically loads the behavioral schema."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(base_dir, 'behavioral_schema.json')
        
        with open(schema_path, 'r') as f:
            self.config = json.load(f)

    def process_telemetry(self, signals: dict, context: str = "conceptual_probing") -> dict:
        """
        Calculates the behavioral score using context-aware weights.
        
        Expected signals format:
        {
            "eye_focus": 0.0 to 1.0,
            "head_stability": 0.0 to 1.0,
            "engagement": 0.0 to 1.0,
            "distraction": 0.0 to 1.0
        }
        """
        # 1. Fetch the specific rules for the current interview context
        context_rules = self.config["context_weights"].get(context)
        if not context_rules:
            raise ValueError(f"Critical Error: Unknown interview context '{context}'")

        weights = context_rules["weights"]
        penalty_weight = context_rules["distraction_penalty"]

        # 2. Extract raw telemetry (defaulting to 0.5 if missing to prevent crashes)
        eye_focus = signals.get("eye_focus", 0.5)
        head_stability = signals.get("head_stability", 0.5)
        engagement = signals.get("engagement", 0.5)
        distraction = signals.get("distraction", 0.0)

        # 3. Calculate Context-Aware Score
        # We reward positive signals based on context weights
        positive_score = (
            (eye_focus * weights["eye_focus"]) +
            (head_stability * weights["head_stability"]) +
            (engagement * weights["engagement"])
        )
        
        # We penalize distraction based on the context's strictness
        distraction_penalty = distraction * penalty_weight
        
        # Final raw math (capped between 0 and 1)
        final_score_raw = max(0.0, min(positive_score - distraction_penalty, 1.0))
        final_score_percentage = round(final_score_raw * 100, 2)

        # 4. Map to Risk Thresholds
        risk_tier = self._determine_risk(final_score_percentage)

        return {
            "behavioral_score": final_score_percentage,
            "context_applied": context,
            "risk_assessment": risk_tier,
            "raw_signals": signals
        }

    def _determine_risk(self, score: float) -> dict:
        """Maps a calculated percentage to the JSON risk thresholds."""
        thresholds = self.config["risk_thresholds"]
        
        if score <= thresholds["high_risk"]["max_score"]:
            return thresholds["high_risk"]
        elif score <= thresholds["moderate_risk"]["max_score"]:
            return thresholds["moderate_risk"]
        else:
            return thresholds["low_risk"]