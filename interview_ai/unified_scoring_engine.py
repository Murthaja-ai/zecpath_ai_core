# interview_ai/unified_scoring_engine.py

# Dynamic cross-round weight dictionaries
ROLE_BASED_WEIGHTS = {
    "fresher": {"ats": 0.20, "screening": 0.30, "deep_interview": 0.50}, # Soft skills & logic matter most
    "experienced": {"ats": 0.30, "screening": 0.20, "deep_interview": 0.50}, # Proven resume matters more
    "technical": {"ats": 0.35, "screening": 0.25, "deep_interview": 0.40},
    "non_technical": {"ats": 0.20, "screening": 0.30, "deep_interview": 0.50}
}

DEFAULT_WEIGHTS = {"ats": 0.30, "screening": 0.30, "deep_interview": 0.40}

def get_weights(candidate_type: str) -> dict:
    """Retrieves the strict weighting multipliers based on the job role."""
    return ROLE_BASED_WEIGHTS.get(candidate_type.lower(), DEFAULT_WEIGHTS)

def check_dealbreakers(ats, screening, interview):
    """VETO SYSTEM: Prevents candidates who catastrophically fail one round from being hired."""
    if ats < 30: return "CRITICAL: Resume failed to meet minimum job requirements."
    if screening < 40: return "CRITICAL: Failed mandatory screening requirements (e.g., clearance, availability)."
    if interview < 50: return "CRITICAL: Failed behavioral or cognitive thresholds during deep interview."
    return None

def generate_unified_profile(candidate_id: str, candidate_type: str, ats_score: float, screening_score: float, interview_score: float):
    """The Master Grand Unifier Pipeline."""
    
    weights = get_weights(candidate_type)
    
    # Check for Veto/Dealbreakers first
    veto_reason = check_dealbreakers(ats_score, screening_score, interview_score)
    
    if veto_reason:
        # If vetoed, mathematically cap their score and force a REJECT
        final_score = min(((ats_score + screening_score + interview_score) / 3), 49.0)
        fit_category = "Low Fit"
        decision = "REJECT"
    else:
        # Normal weighted calculation
        final_score = (
            (ats_score * weights["ats"]) +
            (screening_score * weights["screening"]) +
            (interview_score * weights["deep_interview"])
        )
        
        # Categorize
        if final_score >= 80:
            fit_category = "Excellent Fit"
            decision = "STRONG HIRE"
        elif final_score >= 60:
            fit_category = "Good Fit"
            decision = "CONSIDER"
        else:
            fit_category = "Low Fit"
            decision = "REJECT"

    return {
        "candidate_id": candidate_id,
        "role_type": candidate_type,
        "unified_hiring_score": round(final_score, 2),
        "fit_category": fit_category,
        "final_decision": decision,
        "veto_flag": veto_reason,
        "breakdown": {
            "ats_resume": ats_score,
            "initial_screening": screening_score,
            "deep_ai_interview": interview_score
        },
        "weights_applied": weights
    }