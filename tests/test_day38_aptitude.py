# tests/test_day38_aptitude.py
import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.aptitude_engine import calculate_aptitude_profile

def test_cognitive_engine():
    print("=== Testing Senior Logical Answer ===")
    # Shows structure (first, then, because), risk awareness (alternative, fallback), and scenario hits
    senior_text = "First, I would prioritize the critical tasks. Because time is short, I would delegate the rest. The risk is lower quality, so as an alternative fallback, I would communicate with the client to reduce the MVP scope."
    senior_result = calculate_aptitude_profile(senior_text, scenario_type="deadline_pressure")
    print(json.dumps(senior_result, indent=4))
    
    print("\n=== Testing 'Word Salad' / Panicking Answer ===")
    # Missing sequence, missing risk, missing scenario keywords
    bad_text = "I would just work really hard and try to find a solution to fix everything as fast as possible."
    bad_result = calculate_aptitude_profile(bad_text, scenario_type="deadline_pressure")
    print(json.dumps(bad_result, indent=4))
    
    # Automated Assertions
    assert senior_result["aptitude_score"] > bad_result["aptitude_score"], "Logic Failure: Bad answer scored higher!"
    assert senior_result["breakdown"]["risk_awareness"] == 100.0, "Logic Failure: Failed to detect risk metrics."
    assert bad_result["breakdown"]["structured_thinking"] < 50.0, "Logic Failure: Gave structure points to word salad."
    
    print("\n✅ Unit Tests Passed! The Aptitude & Cognitive logic engine is mathematically sound.")

if __name__ == "__main__":
    test_cognitive_engine()