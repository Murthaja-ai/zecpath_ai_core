# interview_ai/behavioral_engine.py

# Consolidated Dictionaries
HESITATION_WORDS = ["um", "uh", "hmm", "ah"]
UNCERTAINTY_PHRASES = ["not sure", "maybe", "i think", "probably", "i guess", "sorry"]
POSITIVE_WORDS = ["confident", "strong", "good", "success", "achieved", "resolved", "led"]
NEGATIVE_WORDS = ["difficult", "problem", "struggle", "fail", "weak", "terrible", "bad"]
BACKPEDAL_PHRASES = ["wait, no", "actually no", "i don't know", "nevermind"]

def score_hesitation(text: str) -> float:
    text = text.lower()
    count = sum(text.count(word) for word in HESITATION_WORDS)
    return max(0.0, 1.0 - min(count * 0.2, 1.0))

def score_uncertainty(text: str) -> float:
    text = text.lower()
    count = sum(phrase in text for phrase in UNCERTAINTY_PHRASES)
    if count == 0: return 1.0
    if count == 1: return 0.7
    return 0.4

def score_pacing(duration_seconds: float, word_count: int) -> float:
    """Calculates Words Per Second (WPS). Normal human speech is ~2.5 WPS."""
    if duration_seconds <= 0 or word_count == 0: return 0.0
    wps = word_count / duration_seconds
    if 1.5 <= wps <= 3.2: return 1.0  # Perfect pacing
    if 1.0 <= wps < 1.5 or 3.2 < wps <= 4.0: return 0.7 # Too slow or slightly rushing
    return 0.4 # Freezing up or panic-talking

def analyze_sentiment(text: str) -> dict:
    text = text.lower()
    pos = sum(word in text for word in POSITIVE_WORDS)
    neg = sum(word in text for word in NEGATIVE_WORDS)
    
    if pos > neg:
        return {"label": "Positive", "score": min(pos * 0.2, 1.0)}
    elif neg > pos:
        return {"label": "Negative", "score": max(0.0, 1.0 - (neg * 0.2))}
    return {"label": "Neutral", "score": 0.5}

def detect_contradiction(text: str) -> bool:
    """Upgraded to look for backpedaling, not just the word 'but'."""
    text = text.lower()
    return any(phrase in text for phrase in BACKPEDAL_PHRASES)

def calculate_behavioral_profile(text: str, duration_seconds: float) -> dict:
    """The Master Aggregator: Combines confidence, sentiment, and stress into a 0-100 score."""
    if not text.strip():
        return {"behavioral_score": 0.0}

    word_count = len(text.split())
    
    # 1. Calculate Core Confidence (Lack of hesitation/uncertainty + Good pacing)
    hesitation = score_hesitation(text)
    uncertainty = score_uncertainty(text)
    pacing = score_pacing(duration_seconds, word_count)
    
    raw_confidence = (hesitation * 0.35) + (uncertainty * 0.35) + (pacing * 0.30)
    
    # 2. Calculate Sentiment
    sentiment_data = analyze_sentiment(text)
    
    # 3. Contradiction Penalty
    has_contradiction = detect_contradiction(text)
    penalty = 0.2 if has_contradiction else 0.0
    
    # 4. Final Behavioral Score Formula
    # 70% Confidence delivery + 30% Positive Attitude - Contradiction Penalty
    final_score = (raw_confidence * 0.7) + (sentiment_data["score"] * 0.3) - penalty
    final_score = max(0.0, min(1.0, final_score)) # Clamp between 0 and 1
    
    return {
        "behavioral_score": round(final_score * 100, 2),
        "sentiment_label": sentiment_data["label"],
        "breakdown": {
            "confidence_delivery": round(raw_confidence * 100, 2),
            "hesitation_metric": round(hesitation, 2),
            "uncertainty_metric": round(uncertainty, 2),
            "pacing_metric": round(pacing, 2),
            "contradiction_detected": has_contradiction
        }
    }