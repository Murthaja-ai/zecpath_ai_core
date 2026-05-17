def detect_issue(answer):
    """Analyzes the raw text to detect conversational edge cases."""
    if not answer or len(answer.strip()) == 0:
        return "silence"
        
    # If they answer with only 1 word, assume they are confused or need prompting
    if len(answer.split()) < 2:
        return "confusion"
        
    # If they are just repeating the same words over and over (stalling)
    if len(set(answer.split())) < len(answer.split()) / 2:
        return "repeat"
        
    return "valid"