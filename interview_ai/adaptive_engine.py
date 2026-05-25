# interview_ai/adaptive_engine.py

def adapt_question_level(answer_quality: str, confidence_score: float) -> str:
    """Determines the difficulty mode of the next question based on past performance."""
    # Low-quality answer → simplify the next question
    if answer_quality in ["empty", "too_short"]:
        return "simplify"
        
    # Medium → ask for a real-world example
    if answer_quality == "basic":
        return "example"
        
    # High-quality + confident → deeper probe
    if answer_quality == "good" and confidence_score > 0.7:
        return "advanced"
        
    return "normal"

def generate_adaptive_question(base_question: str, mode: str) -> str:
    """Wraps the next base question in a psychological adaptation framing."""
    if mode == "simplify":
        return f"Let me simplify the next topic: {base_question}"
    if mode == "example":
        return f"For this next one, can you give a real-world example: {base_question}?"
    if mode == "advanced":
        return f"You are doing great. Can you handle a complex scenario related to: {base_question}?"
        
    return base_question