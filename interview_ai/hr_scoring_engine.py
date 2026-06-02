# interview_ai/hr_scoring_engine.py

# -------------------------------
# Role-Based Weight Configuration
# -------------------------------
ROLE_WEIGHTS = {
    "fresher": {
        "relevance": 0.25,      # Freshers are given leeway on exact technical relevance
        "communication": 0.35,  # Soft skills matter more
        "confidence": 0.20,
        "consistency": 0.20
    },
    "experienced": {
        "relevance": 0.40,      # Seniors MUST answer the prompt accurately
        "communication": 0.20,
        "confidence": 0.20,
        "consistency": 0.20
    }
}

def score_consistency(contradiction: bool, is_vague: bool) -> float:
    """Translates the Day 34/36 flags into a 0-100 consistency score."""
    if contradiction: return 30.0
    if is_vague: return 60.0
    return 100.0

def generate_explanations(rel: float, comm: float, conf: float, cons: float) -> dict:
    """Translates raw numbers into plain-English sentences for the HR Report."""
    return {
        "relevance": "Highly relevant and on-topic." if rel >= 80 else "Strayed from the core prompt.",
        "communication": "Clear, fluent, and well-structured." if comm >= 80 else "Used filler words or poor structure.",
        "confidence": "Strong delivery with minimal hesitation." if conf >= 80 else "Displayed nervous pacing or uncertainty.",
        "consistency": "Logical and consistent." if cons == 100 else "Contradicted themselves or gave vague details."
    }

def score_single_answer(answer_data: dict, candidate_type: str = "fresher") -> dict:
    """Calculates the weighted score and explanations for a single question."""
    weights = ROLE_WEIGHTS.get(candidate_type, ROLE_WEIGHTS["fresher"])
    
    # Extract scores (assuming inputs are on a 0-100 scale)
    rel = answer_data.get("relevance_score", 0.0)
    comm = answer_data.get("communication_score", 0.0)
    conf = answer_data.get("confidence_score", 0.0)
    
    # Calculate consistency from flags
    cons = score_consistency(
        answer_data.get("contradiction_detected", False), 
        answer_data.get("is_vague", False)
    )
    
    # Master Formula
    final_score = (
        (rel * weights["relevance"]) +
        (comm * weights["communication"]) +
        (conf * weights["confidence"]) +
        (cons * weights["consistency"])
    )
    
    return {
        "question_id": answer_data["question_id"],
        "question_score": round(final_score, 2),
        "metrics": {
            "relevance": round(rel, 2),
            "communication": round(comm, 2),
            "confidence": round(conf, 2),
            "consistency": round(cons, 2)
        },
        "explanations": generate_explanations(rel, comm, conf, cons)
    }

def generate_hr_report(candidate_id: str, candidate_type: str, answer_list: list) -> dict:
    """The Master Aggregator: Normalizes the interview and makes a hiring decision."""
    if not answer_list:
        return {"error": "No answers provided."}
        
    scored_answers = [score_single_answer(ans, candidate_type) for ans in answer_list]
    
    # Normalization: Average the scores regardless of interview length (4 questions vs 8 questions)
    total_score = sum(ans["question_score"] for ans in scored_answers)
    final_interview_score = round(total_score / len(scored_answers), 2)
    
    # Decision Engine
    if final_interview_score >= 75.0:
        decision = "STRONG HIRE"
    elif final_interview_score >= 55.0:
        decision = "CONSIDER"
    else:
        decision = "REJECT"
        
    return {
        "candidate_id": candidate_id,
        "candidate_type": candidate_type,
        "final_hr_score": final_interview_score,
        "decision": decision,
        "breakdown": scored_answers
    }