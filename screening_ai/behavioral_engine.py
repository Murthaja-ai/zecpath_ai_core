import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from models.behavioral_validator import (
    BehavioralIndicators, ConfidenceReport, ConfidenceSignals, 
    SentimentReport, BehaviorFlags
)

class BehavioralAnalysisEngine:
    def __init__(self):
        print("🧠 Booting up Behavioral EQ & Sentiment Analyzer (Company Math Model)...")
        
        # Company Dictionaries
        self.hesitation_words = ["um", "uh", "hmm", "maybe", "not sure", "i think"]
        self.positive_words = ["good", "great", "confident", "skilled", "experienced", "strong"]
        self.negative_words = ["weak", "bad", "difficult", "problem", "not sure", "struggle"]
        self.uncertainty_words = ["maybe", "not sure", "i think", "probably"]

    # --- 1. Confidence Module ---
    def _detect_hesitation(self, text: str) -> float:
        count = sum(text.lower().count(word) for word in self.hesitation_words)
        return min(count / 5.0, 1.0)

    def _response_length_score(self, text: str) -> float:
        word_count = len(text.split())
        if word_count > 12: return 1.0
        elif word_count > 6: return 0.7
        elif word_count > 2: return 0.4
        return 0.1

    def _pace_score(self, text: str, duration_seconds: float) -> float:
        if duration_seconds == 0: return 0.0
        wps = len(text.split()) / duration_seconds
        if 1.5 <= wps <= 3: return 1.0
        elif 1.0 <= wps < 1.5 or 3 < wps <= 4: return 0.7
        return 0.4

    def calculate_confidence(self, text: str, duration_seconds: float) -> dict:
        hesitation = self._detect_hesitation(text)
        length = self._response_length_score(text)
        pace = self._pace_score(text, duration_seconds)
        
        # Company Formula
        confidence = (length * 0.4) + (pace * 0.4) + ((1 - hesitation) * 0.2)
        
        return {
            "confidence_score": round(confidence, 2),
            "signals": {
                "hesitation": round(hesitation, 2),
                "length_score": round(length, 2),
                "pace_score": round(pace, 2)
            }
        }

    # --- 2. Sentiment Module ---
    def detect_sentiment(self, text: str) -> dict:
        text_lower = text.lower()
        pos_count = sum(word in text_lower for word in self.positive_words)
        neg_count = sum(word in text_lower for word in self.negative_words)
        
        if pos_count > neg_count:
            sentiment = "Positive"
            score = min(pos_count / 5.0, 1.0)
        elif neg_count > pos_count:
            sentiment = "Negative"
            score = min(neg_count / 5.0, 1.0)
        else:
            sentiment = "Neutral"
            score = 0.5
            
        return {"sentiment": sentiment, "sentiment_score": round(score, 2)}

    # --- 3. Behavior Rules Module ---
    def detect_behavior_flags(self, text: str) -> dict:
        text_lower = text.lower()
        uncertainty = any(word in text_lower for word in self.uncertainty_words)
        contradiction = "but" in text_lower or "however" in text_lower
        return {"uncertainty": uncertainty, "contradiction": contradiction}

    # --- 4. Master Pipeline ---
    def generate_behavior_report(self, answer_text: str, duration_seconds: float) -> BehavioralIndicators:
        conf_data = self.calculate_confidence(answer_text, duration_seconds)
        sent_data = self.detect_sentiment(answer_text)
        flags_data = self.detect_behavior_flags(answer_text)

        # Calculate final strength string
        raw_strength = (conf_data["confidence_score"] * 0.6) + (sent_data["sentiment_score"] * 0.4)
        if raw_strength >= 0.75: strength_level = "Strong"
        elif raw_strength >= 0.5: strength_level = "Moderate"
        else: strength_level = "Weak"

        # Push through Pydantic to ensure perfect JSON matching
        return BehavioralIndicators(
            confidence=ConfidenceReport(**conf_data),
            sentiment=SentimentReport(**sent_data),
            behavior_flags=BehaviorFlags(**flags_data),
            communication_strength=strength_level
        )

# --- Quick Test ---
if __name__ == "__main__":
    engine = BehavioralAnalysisEngine()
    text = "I am confident in my Python skills and have strong experience"
    duration = 5.0
    
    result = engine.generate_behavior_report(text, duration)
    print(result.model_dump_json(indent=2))