# aggregation_core/test_aggregation.py
import json
from master_orchestrator import CrossRoundOrchestrator

def run_simulation():
    orchestrator = CrossRoundOrchestrator()
    print("📊 Booting Zecpath Phase 11 Aggregation Engine...\n")

    # Scenario 1: Standard Technical Candidate (baseline match)
    print(">>> SCENARIO 1: Complete Technical Profile")
    raw_scores_1 = {
        "ats": 75,
        "screening": 70,
        "hr": 80,
        "technical": 85,  # Note: historical max is 90, so this should curve up!
        "machine_test": 78
    }
    result_1 = orchestrator.process_candidate_profile("C9001", "technical_senior", raw_scores_1)
    print(json.dumps(result_1, indent=2))
    print("\n" + "="*60 + "\n")

    # Scenario 2: Missing Data Demonstration (Machine Test pending)
    print(">>> SCENARIO 2: In-Progress Candidate (Missing Machine Test)")
    raw_scores_2 = {
        "ats": 75,
        "screening": 70,
        "hr": 80,
        "technical": 85,
        "machine_test": None # Still taking the test
    }
    # Using junior role for weight variety
    result_2 = orchestrator.process_candidate_profile("C9002", "technical_junior", raw_scores_2)
    print(json.dumps(result_2, indent=2))

if __name__ == "__main__":
    run_simulation()