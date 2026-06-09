import pytest
from interview_ai.final_hr_module import execute_production_interview_pipeline

def test_production_pipeline_success():
    """Validates a successful, clean candidate evaluation through all engines."""
    good_candidate = {
        "raw_transcript": "I built the database.",
        "historical_metrics": {"ats_score": 80.0, "screening_score": 80.0},
        "interview_metrics": {"communication_sub_scores": [80.0, 80.0], "confidence_system_metric": 80.0, "aptitude_score": 80.0},
        "active_vetoes": []
    }
    result = execute_production_interview_pipeline(good_candidate)
    assert result["final_score"] == 80.0
    assert result["decision"] == "Strong Hire"

def test_production_pipeline_veto_enforcement():
    """Validates that a high-scoring candidate is instantly rejected if a Veto is present."""
    bad_candidate = {
        "raw_transcript": "I bypassed security.",
        "historical_metrics": {"ats_score": 99.0, "screening_score": 99.0},
        "interview_metrics": {"communication_sub_scores": [99.0, 99.0], "confidence_system_metric": 99.0, "aptitude_score": 99.0},
        "active_vetoes": ["SECURITY_VIOLATION"]
    }
    result = execute_production_interview_pipeline(bad_candidate)
    assert result["final_score"] == 0.0
    assert result["decision"] == "Reject"

if __name__ == "__main__":
    pytest.main(["-v", __file__])