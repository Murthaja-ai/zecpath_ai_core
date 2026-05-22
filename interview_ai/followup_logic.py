def should_trigger_followup(answer: str) -> bool:
    """
    Analyzes a candidate's answer to determine if the AI needs to dig deeper.
    """
    if not answer:
        return True
        
    # Heuristic 1: Lazy or incomplete answer (less than 5 words)
    if len(answer.split()) < 5:
        return True
        
    # Heuristic 2: Uncertainty detection
    uncertainty_flags = ["not sure", "i don't know", "maybe", "i guess"]
    if any(flag in answer.lower() for flag in uncertainty_flags):
        return True
        
    return False

def generate_followup(question: str, previous_answer: str) -> str:
    """
    Generates a contextual follow-up prompt.
    """
    if len(previous_answer.split()) < 5:
        return f"Could you please elaborate a bit more on that? I'd love to hear more details."
    
    return f"I understand. Could you provide a specific example related to: {question}?"

if __name__ == "__main__":
    # Quick Test
    test_answer = "I am not sure yet."
    if should_trigger_followup(test_answer):
        print(f"Follow up triggered! AI says: {generate_followup('What are your goals?', test_answer)}")