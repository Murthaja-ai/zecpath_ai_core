import sys
import os
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.report_generator import generate_screening_report

def run_demo():
    print("⚙️ Running Final End-to-End AI Screening Demo...\n")
    
    candidate_id = "C1001"
    job_id = "J2001"

    # Mock Data
    answers = [{
        "question_id": "Q1",
        "original_text": "I have 3 years experience in Python",
        "skills": ["Python"],
        "availability": "Immediate",
        "salary": "6 LPA",
        "is_vague": False,
        "off_topic": False
    }]
    
    scores = [{"question_id": "Q1", "final_score": 85}]
    behavior_reports = [{"communication_strength": "Strong"}]

    # Generate Report
    report = generate_screening_report(
        candidate_id=candidate_id,
        job_id=job_id,
        answers=answers,
        scores=scores,
        behavior_reports=behavior_reports
    )
    
    print("=== 📊 Zecpath AI Final Screening Report ===")
    print(json.dumps(report, indent=4))

if __name__ == "__main__":
    run_demo()