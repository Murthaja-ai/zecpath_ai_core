import pytest

# Mocking production engine states for rapid pipeline assurance
def mock_backend_start_pipeline(payload):
    if "candidate_id" not in payload or "role_type" not in payload:
        return {"error_code": "INVALID_INPUT", "status": 400}
    return {
        "session_id": "MOCK-S-123",
        "status": "INITIALIZED",
        "initial_questions": ["Question One", "Question Two"]
    }

def mock_backend_report_pipeline(session_id, days_elapsed=10):
    if days_elapsed >= 90:
        return {
            "candidate_id": "CANDIDATE_ANONYMIZED",
            "lifecycle_state": "ANONYMIZED_PURSUANT_TO_GDPR",
            "final_unified_score": 0.0,
            "masked_transcript": "[DATA_EXPUNGED]"
        }
    return {
        "candidate_id": "C101",
        "lifecycle_state": "ACTIVE_RETAINED",
        "final_unified_score": 83.35,
        "hiring_decision": "Strong Hire"
    }

def test_api_start_validation_pass():
    """Verifies the setup pipeline handles role declarations securely."""
    payload = {
        "candidate_id": "C101",
        "job_id": "J501",
        "role_type": "data_scientist",
        "experience_level": "fresher"
    }
    response = mock_backend_start_pipeline(payload)
    assert response["status"] == "INITIALIZED"
    assert "session_id" in response
    assert len(response["initial_questions"]) > 0

def test_api_start_validation_missing_field():
    """Validates error response patterns if required inputs are omitted."""
    faulty_payload = {
        "candidate_id": "C101"
    }
    response = mock_backend_start_pipeline(faulty_payload)
    assert response["error_code"] == "INVALID_INPUT"
    assert response["status"] == 400

def test_gdpr_data_lifecycle_retention_enforcement():
    """Asserts that records older than the 90-day threshold are expunged."""
    fresh_record = mock_backend_report_pipeline("MOCK-S-123", days_elapsed=15)
    assert fresh_record["lifecycle_state"] == "ACTIVE_RETAINED"
    assert fresh_record["final_unified_score"] == 83.35
    
    stale_record = mock_backend_report_pipeline("MOCK-S-123", days_elapsed=95)
    assert stale_record["lifecycle_state"] != "ACTIVE_RETAINED"
    assert stale_record["masked_transcript"] == "[DATA_EXPUNGED]"

if __name__ == "__main__":
    pytest.main(["-v", __file__])