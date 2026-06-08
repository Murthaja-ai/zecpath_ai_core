# interview_ai/stability_optimizer.py
import re

# -------------------------------------------------------------------
# 1. TRANSCRIPT CLEANUP & METRIC PRESERVATION
# -------------------------------------------------------------------
def optimize_transcript(raw_text: str) -> dict:
    """Cleans transcripts of noise while counting fillers for fluency scoring."""
    if not raw_text:
        return {"cleaned_text": "", "filler_count": 0}
    
    cleaned = raw_text.lower().strip()
    
    # Track metrics before destroying filler words
    filler_words = r"\b(um|uh|like|you know|basically|actually)\b"
    fillers_found = len(re.findall(filler_words, cleaned))
    
    # Strip fillers, punctuation, and duplicate whitespaces safely
    cleaned = re.sub(filler_words, "", cleaned)
    cleaned = re.sub(r"[^\w\s]", "", cleaned)
    cleaned = re.sub(r"\b(\w+)( \1\b)+", r"\1", cleaned)  # Remove stuttered duplicates ("the the")
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    
    return {
        "cleaned_text": cleaned,
        "filler_count": fillers_found
    }

# -------------------------------------------------------------------
# 2. OUTLIER SMOOTHING & BIAS REDUCTION (Absolute Bound Scaling)
# -------------------------------------------------------------------
def smooth_candidate_scores(sub_scores: list, confidence_score: float) -> float:
    """Removes single-round calculation anomalies without changing the global scale."""
    if not sub_scores:
        return 0.0
    
    global_avg = sum(sub_scores) / len(sub_scores)
    
    # Filter out anomalous spikes (e.g., a 0 caused by a minor API network drop)
    # Only drop scores that deviate by more than 25 points from candidate average
    stable_scores = [s for s in sub_scores if abs(s - global_avg) <= 25]
    if not stable_scores:
        stable_scores = sub_scores
        
    smoothed_base = sum(stable_scores) / len(stable_scores)
    
    # Bias Reduction: Blend confidence vector gracefully (90% score weight, 10% AI confidence)
    final_adjusted = (smoothed_base * 0.90) + (confidence_score * 0.10)
    return round(max(0.0, min(100.0, final_adjusted)), 2)

# -------------------------------------------------------------------
# 3. FOLLOW-UP STATE LOCK PROTECTION
# -------------------------------------------------------------------
def evaluate_followup_state(quality_metric: str, retry_count: int) -> str:
    """Prevents the AI playlist from entering infinite pushback loops."""
    if retry_count >= 2:
        return "TERMINATE_LOOP_PROCEED_TO_NEXT_ROUND"
    
    mapping = {
        "empty": "CLARIFY_PROMPT",
        "too_short": "CLARIFY_PROMPT",
        "uncertain": "SIMPLIFY_PROMPT"
    }
    return mapping.get(quality_metric.lower(), "PROCEED_NORMALLY")