# technical_ai/evaluation_engine.py
import json
import os

class TechnicalScoringEngine:
    def __init__(self):
        """Initializes the engine and dynamically loads the scoring rubrics."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        rubric_path = os.path.join(base_dir, 'scoring_rubrics.json')
        
        with open(rubric_path, 'r') as f:
            self.config = json.load(f)

    def _detect_depth(self, text: str) -> dict:
        """Evaluates if the answer is superficial or deeply understood."""
        text_lower = text.lower()
        words = text_lower.split()
        word_count = len(words)
        
        # Enterprise keywords indicating deep technical reasoning
        deep_keywords = ["because", "architecture", "optimize", "scalable", "tradeoff", "memory", "performance", "under the hood"]
        matches = sum(1 for word in deep_keywords if word in text_lower)

        if word_count > 20 and matches >= 2:
            return {"label": "deep", "score": 1.0}
        elif word_count > 10 or matches >= 1:
            return {"label": "moderate", "score": 0.7}
        return {"label": "shallow", "score": 0.4}

    def _evaluate_logic(self, text: str) -> float:
        """Scores logical flow using resilient reasoning markers."""
        text_lower = text.lower()
        reasoning_markers = ["first", "then", "subsequently", "therefore", "approach", "step", "prioritize", "however"]
        
        if sum(1 for marker in reasoning_markers if marker in text_lower) >= 2:
            return 1.0
        elif len(text.split()) > 15:
            return 0.7
        return 0.4

    def _evaluate_real_world(self, text: str) -> float:
        """Checks for production/practical applicability."""
        text_lower = text.lower()
        practical_terms = ["production", "real-world", "example", "use case", "deployment", "client", "scale", "scenario"]
        
        if any(term in text_lower for term in practical_terms):
            return 1.0
        return 0.4

    def process_answer(self, answer: str, question_type: str, difficulty: str, is_correct: bool = True) -> dict:
        """The master pipeline for scoring a technical answer based on dynamic rubrics."""
        
        # 1. Run raw text analysis
        accuracy_score = 1.0 if is_correct else 0.4
        depth_result = self._detect_depth(answer)
        logic_score = self._evaluate_logic(answer)
        real_world_score = self._evaluate_real_world(answer)

        # 2. Map raw text scores to all possible rubric parameters
        metric_pool = {
            "accuracy": accuracy_score,
            "depth": depth_result["score"],
            "logic": logic_score,
            "real_world": real_world_score,
            "optimization": depth_result["score"],   # Ties optimization to depth
            "architecture": depth_result["score"],   # Ties architecture to depth
            "scalability": logic_score,              # Ties scalability to logic
            "trade_offs": real_world_score,          # Ties trade-offs to real-world experience
            "decision_quality": logic_score
        }

        # 3. Fetch specific weights for this question type
        weights = self.config["question_types"].get(question_type, {}).get("weights", {})
        if not weights:
            raise ValueError(f"Critical Error: Unknown question type '{question_type}'")

        # 4. Calculate the weighted base score safely
        base_score = sum(metric_pool[key] * weight for key, weight in weights.items())

        # 5. Apply Difficulty Normalization (Hysteresis alignment)
        multiplier = self.config["difficulty_multipliers"].get(difficulty, 1.0)
        normalized_score = min(base_score * multiplier, 1.0) # Cap at 100%

        return {
            "raw_score": round(base_score * 100, 2),
            "final_normalized_score": round(normalized_score * 100, 2),
            "depth_classification": depth_result["label"],
            "parameter_breakdown": {
                "accuracy": accuracy_score,
                "depth": depth_result["score"],
                "logic": logic_score,
                "real_world": real_world_score
            }
        }