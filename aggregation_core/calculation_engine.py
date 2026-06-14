# aggregation_core/calculation_engine.py
import json
import os

class AggregationMathEngine:
    def __init__(self):
        """Loads the weights and normalization limits dynamically."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(base_dir, 'weights_config.json')
        
        with open(config_path, 'r') as f:
            data = json.load(f)
            self.weights_schema = data["role_weights"]
            self.cohort_bounds = data["cohort_normalization_bounds"]

    def _normalize_score(self, round_name: str, raw_score: float) -> float:
        """Applies Min-Max scaling based on historical cohort difficulty."""
        bounds = self.cohort_bounds.get(round_name)
        if not bounds:
            return raw_score  # Fallback if no bounds defined

        c_min = bounds["historical_min"]
        c_max = bounds["historical_max"]

        # Prevent divide by zero and clamp edges
        if raw_score <= c_min: return 0.0
        if raw_score >= c_max: return 100.0

        # True Min-Max Scaling Formula
        normalized = ((raw_score - c_min) / (c_max - c_min)) * 100
        return round(normalized, 2)

    def calculate_unified_score(self, role_type: str, candidate_scores: dict) -> dict:
        """
        Dynamically calculates the final score, applying dynamic residual re-weighting
        to gracefully handle rounds that are missing or currently pending.
        """
        # 1. Fetch intended weights
        target_weights = self.weights_schema.get(role_type)
        if not target_weights:
            raise ValueError(f"System Error: Role type '{role_type}' is not configured.")

        # 2. Identify missing rounds to redistribute weight
        active_weight_sum = 0.0
        active_scores = {}
        
        for stage, weight in target_weights.items():
            if stage in candidate_scores and candidate_scores[stage] is not None:
                active_weight_sum += weight
                # Normalize while we loop
                active_scores[stage] = self._normalize_score(stage, candidate_scores[stage])
            elif weight > 0:
                # Round is missing but supposed to carry weight
                pass

        if active_weight_sum == 0.0:
            return {"final_score": 0.0, "status": "No valid data provided."}

        # 3. Dynamic Re-Weighting (The Residual Distribution)
        # We scale the active weights up so they equal 1.0 (100%)
        final_score = 0.0
        applied_weights = {}

        for stage, norm_score in active_scores.items():
            adjusted_weight = target_weights[stage] / active_weight_sum
            applied_weights[stage] = round(adjusted_weight, 3)
            final_score += (norm_score * adjusted_weight)

        return {
            "final_percentage": round(final_score, 2),
            "normalized_raw_scores": active_scores,
            "dynamically_applied_weights": applied_weights,
            "missing_rounds_handled": active_weight_sum < 1.0
        }