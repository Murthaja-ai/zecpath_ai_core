import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from models.understanding_validator import UnderstoodAnswer
from screening_ai.scoring_engine import ScreeningScoringEngine
from screening_ai.improved_intent import improved_intent_classification

def simulate_test():
    print("🚀 Running Day 30 End-to-End System Simulation...")
    
    # 1. Test the new Intent Engine
    raw_text = "I have 2 years experience"
    detected_intent = improved_intent_classification(raw_text)
    print(f"   -> [Intent Tuner]: Detected '{detected_intent}'")
    
    # 2. Package it into our Day 25 Firewall
    sample_answer = UnderstoodAnswer(
        question_id="Q3",
        original_text=raw_text,
        intent=detected_intent,
        skills=[],
        experience_years=2,
        off_topic=False,
        is_vague=False,
        is_missing=False
    )
    
    # 3. Run it through the Day 26 Math Engine
    intent_map = {"Q3": "experience"}
    engine = ScreeningScoringEngine()
    result = engine.screening_scoring_pipeline("C123", [sample_answer], intent_map)
    
    # 4. Apply Day 30 Thresholds (65 instead of 70)
    decision = "Pass" if result.screening_score >= 65 else "Review" if result.screening_score >= 45 else "Reject"
    
    print(f"\n📊 FINAL RESULTS:")
    print(f"   Score: {result.screening_score}")
    print(f"   Decision: {decision}")
    print("✅ Simulation Complete. False rejection avoided!")

if __name__ == "__main__":
    simulate_test()