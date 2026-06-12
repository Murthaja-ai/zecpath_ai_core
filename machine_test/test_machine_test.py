# machine_test/test_machine_test.py
from scoring_pipeline import PracticalScoringPipeline
import json

def run_simulation():
    pipeline = PracticalScoringPipeline()

    print("🛡️ Booting Zecpath Phase 10 Machine Test Pipeline...\n")

    # --- Scenario 1: Honest Senior Developer doing a File Task ---
    print(">>> SCENARIO 1: Honest Developer (File Task)")
    good_code = """
def parse_csv(file_path):
    try:
        with open(file_path, 'r') as f:
            return [line.strip().split(',') for line in f]
    except Exception as e:
        return []
    """
    exec_data_1 = {"passed": 20, "total": 20, "runtime_seconds": 3.2, "attempts": 2, "time_taken_minutes": 25}
    integrity_data_1 = {"integrity_score": 98, "risk_level": "Low Risk"}
    
    res1 = pipeline.process_machine_test("file_based_task", exec_data_1, good_code, integrity_data_1)
    print(json.dumps(res1, indent=2))
    print("\n" + "="*50 + "\n")

    # --- Scenario 2: Cheater doing a Coding Problem ---
    print(">>> SCENARIO 2: Cheating Candidate (Coding Problem)")
    stolen_code = "def reverse(s): return s[::-1]"
    
    # Perfect execution data
    exec_data_2 = {"passed": 10, "total": 10, "runtime_seconds": 0.1, "attempts": 1, "time_taken_minutes": 2}
    # Failed Integrity Check (from Phase 9)
    integrity_data_2 = {"integrity_score": 30, "risk_level": "High Risk / Flagged System Breach"}

    res2 = pipeline.process_machine_test("coding_problem", exec_data_2, stolen_code, integrity_data_2)
    print(json.dumps(res2, indent=2))

if __name__ == "__main__":
    run_simulation()