import hashlib
import statistics

# -------------------------------
# Safe Value Handler (Boundary Protection)
# -------------------------------
def safe_value(v, default=0.0):
    """Ensures incoming score is a valid float precisely between 0 and 100."""
    try:
        v = float(v)
    except (ValueError, TypeError):
        return default
    return max(0.0, min(v, 100.0))

def validate_scores(scores):
    return {k: safe_value(v) for k, v in scores.items()}

# -------------------------------
# Stable Variance Aggregation (The Math Engine)
# -------------------------------
def variance_aggregation(scores):
    """Calculates final score, applying penalties for extreme inconsistencies."""
    sanitized = validate_scores(scores)
    if not sanitized:
        return 0.0
    
    values = list(sanitized.values())
    mean_score = sum(values) / len(values)
    
    # Standard Deviation Penalty (Protects against "Brilliant Jerks")
    if len(values) > 1:
        stdev = statistics.stdev(values)
        if stdev > 25.0: # High inconsistency flag
            mean_score -= (stdev * 0.5) 
    
    return round(max(0.0, mean_score), 2)

# -------------------------------
# Final Decision & Cryptographic Logic
# -------------------------------
def final_decision(score, integrity_flags=0):
    if integrity_flags > 0:
        return "REJECTED (Integrity Violation)"
    if score >= 85:
        return "SELECTED"
    elif score >= 70:
        return "HOLD / REVIEW"
    return "REJECTED"

def generate_secure_hash(candidate_id, decision):
    """Simulates the Day 61 Vault to ensure data immutability."""
    payload = f"{candidate_id}:{decision}".encode('utf-8')
    return hashlib.sha256(payload).hexdigest()

# -------------------------------
# V1.0 Release Pipeline
# -------------------------------
def release_pipeline(candidate_id, scores, integrity_flags=0):
    final_score = variance_aggregation(scores)
    
    # Phase 9 Hard Gate Override
    if integrity_flags > 0:
        final_score = 0.0

    decision = final_decision(final_score, integrity_flags)
    vault_hash = generate_secure_hash(candidate_id, decision)

    return {
        "candidate_id": candidate_id,
        "final_score": final_score,
        "decision": decision,
        "integrity_flags": integrity_flags,
        "vault_hash": vault_hash,
        "status": "RELEASE_READY"
    }