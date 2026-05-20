ERROR_RESPONSES = {
    "missing": "I didn’t receive your response. Could you please answer?",
    "poor_audio": "The audio is unclear due to background noise. Could you please repeat?",
    "unclear": "Can you please explain that more clearly?",
    "language_mix": "I detect multiple languages. Would you prefer to continue in Malayalam or English?",
    "incomplete": "Could you provide a few more details?",
    "fallback": "Let’s move to the next question."
}

def get_error_response(issue: str) -> str:
    """Returns the polite, spoken response for the detected edge case."""
    return ERROR_RESPONSES.get(issue, ERROR_RESPONSES["fallback"])