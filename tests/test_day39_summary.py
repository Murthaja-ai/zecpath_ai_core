# tests/test_day39_summary.py
import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.summary_generator import generate_interview_summary

def test_summary_engine():
    # Mock Data for a brilliant candidate
    good_hr = {"final_hr_score": 90.0}
    good_apt = {"aptitude_score": 88.0, "breakdown": {"structured_thinking": 90.0, "risk_awareness": 100.0}}
    good_comm = 85.0
    good_beh = {"behavioral_score": 90.0, "contradiction_detected": False}

    # Mock Data for a panicking, backpedaling candidate
    bad_hr = {"final_hr_score": 45.0}
    bad_apt = {"aptitude_score": 40.0, "breakdown": {"structured_thinking": 30.0, "risk_awareness": 20.0}}
    bad_comm = 40.0
    bad_beh = {"behavioral_score": 30.0, "contradiction_detected": True}

    print("=== Testing Outstanding Candidate Summary ===")
    good_report = generate_interview_summary("CAND-GOOD", good_hr, good_apt, good_comm, good_beh)
    print(json.dumps(good_report, indent=4))

    print("\n=== Testing High-Risk Candidate Summary ===")
    bad_report = generate_interview_summary("CAND-RISK", bad_hr, bad_apt, bad_comm, bad_beh)
    print(json.dumps(bad_report, indent=4))

    # Automated Assertions
    assert "CRITICAL" in bad_report["structured_insights"]["risk_flags"][0], "Logic Failure: Did not detect the critical contradiction flag!"
    assert good_report["decision"] == "STRONG HIRE", "Logic Failure: Composite score grading is broken."
    
    print("\n✅ Unit Tests Passed! The Summary Engine successfully translates raw data into executive HR insights.")

if __name__ == "__main__":
    test_summary_engine()