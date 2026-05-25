# tests/test_day34_followup.py
import sys
import os

# --- PATH FIX ---
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)
# ----------------

from interview_ai.followup_engine import detect_answer_quality

def test_followup():
    print("🧪 Running Unit Test: detect_answer_quality...")
    
    # Test a 2-word answer
    result = detect_answer_quality("I worked")
    
    # Assert forces the code to crash if the result is wrong.
    # If it passes silently, the test is successful!
    assert result == "too_short", f"Test failed! Expected 'too_short', got '{result}'"
    
    print("✅ Unit Test Passed! Answer quality detection works perfectly.")

if __name__ == "__main__":
    test_followup()