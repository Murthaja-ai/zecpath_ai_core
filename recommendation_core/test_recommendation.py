# recommendation_core/test_recommendation.py
import json
from master_recommendation import FinalRecommendationOrchestrator

def run_simulation():
    orchestrator = FinalRecommendationOrchestrator()
    print("⚖️ Booting Zecpath Phase 12 Recommendation Engine...\n")

    # Scenario 1: The Brilliant Cheater
    print(">>> SCENARIO 1: The 'Brilliant Cheater' (High Score, High Integrity Risk)")
    phase_scores = {"ats": 90, "screening": 95, "hr": 92, "tech": 99, "machine": 98}
    # Raw score is an incredible 95%, but integrity is High Risk
    res1 = orchestrator.process_final_decision("C10001", 95.0, phase_scores, "Low Risk", "High Risk")
    print(json.dumps(res1, indent=2))
    print("\n" + "="*60 + "\n")

    # Scenario 2: Standard Strong Hire
    print(">>> SCENARIO 2: Honest Senior Developer")
    phase_scores_2 = {"ats": 85, "screening": 80, "hr": 88, "tech": 90, "machine": 85}
    res2 = orchestrator.process_final_decision("C10002", 86.0, phase_scores_2, "Low Risk", "Low Risk")
    print(json.dumps(res2, indent=2))

if __name__ == "__main__":
    run_simulation()