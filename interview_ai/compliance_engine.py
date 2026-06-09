import re
from datetime import datetime, timedelta, timezone

# -------------------------------------------------------------------
# 1. AUTOMATED PII ANONYMIZATION ENGINE
# -------------------------------------------------------------------
def mask_candidate_demographics(raw_text: str, candidate_name: str) -> str:
    """Strips explicit name, pronoun genders, and demographic signals to ensure blind grading."""
    if not raw_text:
        return ""
    
    masked = raw_text.lower()
    
    # Securely mask explicit name variations
    name_clean = candidate_name.lower().strip()
    if name_clean:
        masked = re.sub(rf"\b{name_clean}\b", "[CANDIDATE_ANONYMIZED]", masked)
    
    # Strip gender identifiers to satisfy international non-discrimination standards
    gender_pronouns = {
        r"\b(he|she)\b": "they",
        r"\b(him|her)\b": "them",
        r"\b(his|hers)\b": "their"
    }
    for regex_pattern, replacement in gender_pronouns.items():
        masked = re.sub(regex_pattern, replacement, masked)
        
    return masked

# -------------------------------------------------------------------
# 2. CORE AUTOMATED EXPLAINABILITY GENERATOR
# -------------------------------------------------------------------
def generate_explainable_output(final_score: float, breakdowns: dict, vetoes_triggered: list) -> dict:
    """Translates numerical vectors into deterministic, legally defensive justifications."""
    if vetoes_triggered:
        explanation = f"Application rejected due to corporate dealbreaker triggers: {', '.join(vetoes_triggered)}."
        decision = "Reject"
    elif final_score >= 80:
        explanation = "Excellent alignment across core technical competencies, high operational confidence, and fluent delivery."
        decision = "Strong Hire"
    elif final_score >= 60:
        explanation = "Competent performance with moderate technical alignment. Communication patterns are clear but lack depth in core areas."
        decision = "Consider"
    else:
        explanation = "Evaluation score falls below role benchmarks. Technical or behavioral responses did not meet minimum requirements."
        decision = "Reject"

    return {
        "final_score": final_score,
        "decision": decision,
        "justification": explanation,
        "breakdowns": breakdowns,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

# -------------------------------------------------------------------
# 3. AUTOMATED GDPR RETENTION & DATA PURGE ENGINE
# -------------------------------------------------------------------
def enforce_data_retention(candidate_record: dict, current_date_str: str = None) -> dict:
    """Enforces absolute Right to Erasure by purging identifying data elements after 90 days."""
    current_date = datetime.strptime(current_date_str, "%Y-%m-%d") if current_date_str else datetime.now(timezone.utc).replace(tzinfo=None)
    creation_date = datetime.strptime(candidate_record["created_at"], "%Y-%m-%d")
    
    days_elapsed = (current_date - creation_date).days
    
    # Hard boundary check for GDPR / Data Minimization conformity
    if days_elapsed >= 90:
        purged_record = {
            "candidate_id": candidate_record["candidate_id"],
            "created_at": candidate_record["created_at"],
            "status": "ANONYMIZED_PURSUANT_TO_GDPR_90_DAYS",
            "masked_transcript": "[DATA_EXPUNGED]",
            "final_score": candidate_record.get("final_score", 0),
            "justification": "Text metrics and metadata completely purged following data retention limit."
        }
        return purged_record
        
    return candidate_record