# tests/test_day41_unified.py
import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.unified_scoring_engine import generate_unified_profile

def test_unified_engine():
    print("=== Testing Outstanding Candidate ===")
    good_cand = generate_unified_profile("CAND-01", "experienced", 90.0, 95.0, 88.0)
    print(json.dumps(good_cand, indent=4))

    print("\n=== Testing The 'Dealbreaker' Flaw ===")
    # Candidate aces the resume and interview, but catastrophically fails the background screening
    flawed_cand = generate_unified_profile("CAND-02", "experienced", 100.0, 10.0, 100.0)
    print(json.dumps(flawed_cand, indent=4))

    # Automated Assertions
    assert good_cand["final_decision"] == "STRONG HIRE", "Logic Failure: Good candidate rejected."
    
    # If the company's original broken math ran, flawed_cand would score an 80.0. 
    # Our system must VETO them.
    assert flawed_cand["final_decision"] == "REJECT", "CRITICAL FAILURE: Dealbreaker Veto did not trigger!"
    assert flawed_cand["veto_flag"] is not None, "CRITICAL FAILURE: Veto reason missing."
    
    print("\n✅ Unit Tests Passed! The Unified Scoring Engine successfully calculates weights and enforces dealbreakers.")

if __name__ == "__main__":
    test_unified_engine()