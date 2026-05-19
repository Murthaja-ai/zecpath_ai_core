import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.improved_intent import improved_intent_classification

def test_intent():
    print("🧪 Running Test: Improved Intent Tuner...")
    text = "I worked as a developer for 2 years"
    result = improved_intent_classification(text)
    assert result == "experience", f"Failed: Got {result}"
    print("✅ Test Passed! Keyword intent mapping works perfectly.")

if __name__ == "__main__":
    test_intent()