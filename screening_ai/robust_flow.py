# -------------------------------
# Extended Edge Case Detection
# -------------------------------
def detect_edge_case(answer: str, confidence: float = 1.0) -> str:
    """Analyzes text and audio metadata to detect severe real-world edge cases."""
    
    if not answer or len(answer.strip()) == 0:
        return "missing"
        
    if confidence < 0.6:
        return "poor_audio"
        
    if any(word in answer.lower() for word in ["um", "uh"]) and len(answer.split()) < 3:
        return "unclear"
        
    # Regional code-switching detection (Kerala context)
    if any(lang in answer.lower() for lang in ["hai", "enna", "chetta", "bhai", "pakshe"]):
        return "language_mix"
        
    if len(answer.split()) < 2:
        return "incomplete"
        
    return "valid"

# -------------------------------
# Adaptive Flow Handler
# -------------------------------
def handle_edge_case(answer: str, confidence: float, retry_count: int) -> str:
    """Determines the next state machine action based on the edge case."""
    issue = detect_edge_case(answer, confidence)
    
    # Hard safety fallback to prevent infinite loops
    if retry_count >= 2:
        return "skip_question"
        
    if issue == "missing":
        return "retry"
    elif issue == "poor_audio":
        return "ask_repeat_audio"
    elif issue == "unclear":
        return "simplify_question"
    elif issue == "language_mix":
        return "switch_language"
    elif issue == "incomplete":
        return "ask_detail"
        
    return "next"