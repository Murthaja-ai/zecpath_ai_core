# tests/test_day37_hr_scoring.py
import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.hr_scoring_engine import generate_hr_report

def test_master_scoring_pipeline():
    # Mock data coming from Day 35 (Communication) and Day 36 (Behavior)
    mock_answers = [
        {
            "question_id": "Q1",
            "relevance_score": 90.0,
            "communication_score": 85.0,
            "confidence_score": 80.0,
            "contradiction_detected": False,
            "is_vague": False
        },
        {
            "question_id": "Q2",
            "relevance_score": 40.0, # Terribly off-topic answer
            "communication_score": 50.0,
            "confidence_score": 45.0,
            "contradiction_detected": True, # Backpedaled
            "is_vague": True
        }
    ]
    
    print("=== Testing Experienced Candidate Pipeline ===")
    experienced_report = generate_hr_report("CAND-EX1", "experienced", mock_answers)
    print(json.dumps(experienced_report, indent=4))
    
    # Automated Assertions
    assert experienced_report["decision"] == "CONSIDER", "Logic Failure: Score aggregation is broken."
    assert len(experienced_report["breakdown"]) == 2, "Normalization logic failed to process all questions."
    
    print("\n✅ Unit Tests Passed! The Master HR Report Generator works perfectly.")

if __name__ == "__main__":
    test_master_scoring_pipeline()