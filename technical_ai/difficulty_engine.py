# technical_ai/difficulty_engine.py

# The ordered tiers of difficulty
DIFFICULTY_TIERS = ["basic", "intermediate", "advanced"]

def evaluate_difficulty_transition(current_difficulty: str, current_score: float, positive_streak: int, negative_streak: int, questions_asked: int) -> dict:
    """
    Adjusts the interview difficulty using a Hysteresis (Streak) model.
    Prevents volatile 'yo-yo' scoring by requiring 2 consecutive high/low scores to change tiers.
    """
    
    # Cold-Start Protection: Do not drop a candidate until they've answered at least 2 questions
    if questions_asked < 2 and current_score < 0.40:
        return {
            "new_difficulty": current_difficulty,
            "positive_streak": 0,
            "negative_streak": negative_streak + 1,
            "status_message": "Cold-start protection active. Score logged, no drop applied."
        }

    # Track Streaks based on the current score
    if current_score >= 0.80:
        positive_streak += 1
        negative_streak = 0
    elif current_score <= 0.40:
        negative_streak += 1
        positive_streak = 0
    else:
        # Neutral score resets both streaks
        positive_streak = 0
        negative_streak = 0

    current_index = DIFFICULTY_TIERS.index(current_difficulty)

    # Level UP Trigger: 2 consecutive high scores
    if positive_streak >= 2 and current_index < len(DIFFICULTY_TIERS) - 1:
        return {
            "new_difficulty": DIFFICULTY_TIERS[current_index + 1],
            "positive_streak": 0,  # Reset after promotion
            "negative_streak": 0,
            "status_message": "Candidate promoted to harder tier."
        }

    # Level DOWN Trigger: 2 consecutive low scores
    if negative_streak >= 2 and current_index > 0:
        return {
            "new_difficulty": DIFFICULTY_TIERS[current_index - 1],
            "positive_streak": 0,
            "negative_streak": 0,  # Reset after demotion
            "status_message": "Candidate demoted to easier tier."
        }

    # Default: Stay at current difficulty
    return {
        "new_difficulty": current_difficulty,
        "positive_streak": positive_streak,
        "negative_streak": negative_streak,
        "status_message": "Difficulty maintained."
    }