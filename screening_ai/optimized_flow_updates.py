# screening_ai/optimized_flow_updates.py

def adaptive_retry_logic(issue, retry_count):
    """Smarter routing logic that adapts to the candidate's struggle level."""
    if issue == "silence":
        if retry_count == 0:
            return "retry"
        elif retry_count == 1:
            return "simplify_question" # AI realizes the user might be stuck
        else:
            return "skip_question"
            
    if issue == "confusion":
        return "clarify"
        
    if issue == "repeat":
        return "ask_example"
        
    return "next"