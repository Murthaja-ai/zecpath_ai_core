# optimization_core/score_refiner.py
import math

class StatisticalScoreRefiner:
    @staticmethod
    def calculate_consistency_adjustment(scores: dict, penalty_weight: float = 5.0) -> float:
        """
        Calculates mathematical stability using standard deviation.
        Penalizes extreme volatility across individual interview rounds.
        """
        # Filter out missing rounds (None values) and convert to floats
        values = [float(v) for v in scores.values() if v is not None]
        if len(values) < 2:
            return 0.0
            
        # Calculate Standard Deviation
        mean = sum(values) / len(values)
        variance = sum((x - mean) ** 2 for x in values) / len(values)
        std_deviation = math.sqrt(variance)

        # High variance (std_dev > 15) indicates unpredictable, erratic performance
        if std_deviation > 15.0:
            return -penalty_weight
        # Low variance (std_dev < 5.0) indicates highly reliable consistency
        elif std_deviation < 5.0:
            return +5.0
            
        return 0.0

    @classmethod
    def generate_refined_score(cls, scores: dict, base_score: float) -> float:
        """Applies the consistency adjustment within strict 0-100 mathematical boundaries."""
        adjustment = cls.calculate_consistency_adjustment(scores)
        return max(min(base_score + adjustment, 100.0), 0.0)