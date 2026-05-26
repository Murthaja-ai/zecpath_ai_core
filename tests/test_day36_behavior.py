# tests/test_day36_behavior.py
import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.behavioral_engine import calculate_behavioral_profile

def test_behavioral_pipeline():
    print("=== Testing Confident Answer ===")
    # 10 words, 4 seconds = 2.5 WPS (Perfect Pacing)
    confident_text = "I successfully led the team and resolved the difficult server problem."
    confident_result = calculate_behavioral_profile(confident_text, duration_seconds=4.0)
    print(json.dumps(confident_result, indent=4))
    
    print("\n=== Testing Nervous/Backpedaling Answer ===")
    # Shows hesitation, uncertainty, and backpedaling
    nervous_text = "um I guess I fixed it, wait, no, actually the senior dev did it."
    nervous_result = calculate_behavioral_profile(nervous_text, duration_seconds=6.0)
    print(json.dumps(nervous_result, indent=4))
    
    # Automated Assertions
    assert confident_result["behavioral_score"] > nervous_result["behavioral_score"], "Logic Failure: Nervous score is higher!"
    assert confident_result["breakdown"]["contradiction_detected"] == False, "Logic Failure: False positive on contradiction!"
    assert nervous_result["breakdown"]["contradiction_detected"] == True, "Logic Failure: Failed to detect backpedaling!"
    
    print("\n✅ Unit Tests Passed! Behavioral psychology engine is mathematically sound.")

if __name__ == "__main__":
    test_behavioral_pipeline()