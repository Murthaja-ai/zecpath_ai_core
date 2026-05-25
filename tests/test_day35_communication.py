# tests/test_day35_communication.py
import sys
import os
import json

# --- PATH FIX ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)
# ----------------

from interview_ai.communication_engine import calculate_communication_score
from interview_ai.normalization import normalize_score

def test_communication_pipeline():
    print("=== Testing Strong Answer ===")
    strong_text = "I have experience in Python because I worked on backend systems."
    strong_result = calculate_communication_score(strong_text)
    print(json.dumps(strong_result, indent=4))
    
    print("\n=== Testing Weak Answer (Filler Words) ===")
    weak_text = "um I like worked on um projects."
    weak_result = calculate_communication_score(weak_text)
    print(json.dumps(weak_result, indent=4))
    
    # Automated Assertions
    assert strong_result["communication_score"] > weak_result["communication_score"], "Logic Failure: Weak score is higher than strong score!"
    assert strong_result["communication_score"] > 0, "Score calculation failed."
    
    print("\n✅ Unit Tests Passed! The objective grading engine is mathematically sound.")

if __name__ == "__main__":
    test_communication_pipeline()