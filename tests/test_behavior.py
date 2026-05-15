import os
import sys

# Add the root directory to the system path so it can find our modules
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.behavioral_engine import BehavioralAnalysisEngine

def test_behavior():
    print("🧪 Running Automated Test: Behavioral Engine...")
    engine = BehavioralAnalysisEngine()
    
    text = "I am confident and experienced"
    duration = 5.0
    
    # Run the engine
    result = engine.generate_behavior_report(text, duration)
    
    # Extract the strength from the Pydantic object
    strength = result.communication_strength
    
    # Assert it meets the company's requirement
    assert strength in ["Strong", "Moderate"], f"Test Failed! Got {strength}"
    
    print(f"✅ Test Passed! Communication Strength was correctly evaluated as: {strength}")

if __name__ == "__main__":
    test_behavior()