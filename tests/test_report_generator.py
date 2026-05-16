import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.report_generator import generate_screening_report

def test_report():
    print("🧪 Running Test: Screening Report Generator...")
    report = generate_screening_report("C1", "J1", [], [], [])
    
    assert "candidate_id" in report
    assert report["candidate_id"] == "C1"
    assert report["job_id"] == "J1"
    print("✅ Test Passed! Report successfully generated.")

if __name__ == "__main__":
    test_report()