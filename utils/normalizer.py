class ScoreNormalizer:
    def __init__(self):
        print("📈 Booting up Statistical Normalizer (Curve Grading)...")

    def normalize_scores(self, candidates):
        """
        Applies Min-Max Normalization to a list of candidate dictionaries.
        Formula: (score - min) / (max - min)
        """
        if not candidates:
            return []

        # 1. Extract all final scores to find the Min and Max
        scores = [c.get("final_score", 0) for c in candidates]
        min_score = min(scores)
        max_score = max(scores)

        # Edge Case: If everyone got the exact same score, or there's only 1 candidate
        if max_score == min_score:
            for c in candidates:
                c["normalized_score"] = 1.0  # Give them a perfect curve
            return candidates

        # 2. Apply the mathematical curve to every candidate
        for c in candidates:
            raw_score = c.get("final_score", 0)
            
            # The Min-Max Formula
            curved_score = (raw_score - min_score) / (max_score - min_score)
            
            c["normalized_score"] = round(curved_score, 3)

        return candidates