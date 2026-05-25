# interview_ai/normalization.py

def normalize_score(score: float, min_val: float = 0.0, max_val: float = 100.0) -> float:
    """
    Normalizes a score to a standard 0-100 scale to reduce algorithmic bias.
    Ensures that extreme outliers are contained within the boundary.
    """
    # Prevent division by zero if min and max are somehow identical
    if max_val == min_val:
        return 0.0
        
    normalized = (score - min_val) / (max_val - min_val)
    
    # Cap the results between 0 and 100
    final_score = round(normalized * 100, 2)
    final_score = max(0.0, min(100.0, final_score))
    
    return final_score