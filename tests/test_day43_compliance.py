# tests/test_day43_compliance.py
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.compliance_engine import mask_candidate_demographics, generate_explainable_output, enforce_data_retention

def test_ethical_pipeline():
    print("=== Running Day 43 Ethical & Compliance Verification ===")

    # 1. Test Demographic and PII Scrubbing Logic
    raw_transcript = "He completed the project efficiently. Murthaja showed great focus."
    masked_output = mask_candidate_demographics(raw_transcript, candidate_name="Murthaja")
    print(f"Raw Input:   '{raw_transcript}'")
    print(f"Masked Text: '{masked_output}'")
    assert "murthaja" not in masked_output
    assert "they" in masked_output

    # 2. Test Algorithmic Explainability Format
    explainable_payload = generate_explainable_output(
        final_score=84.5, 
        breakdowns={"ats": 85, "hr": 84}, 
        vetoes_triggered=[]
    )
    print(f"\nAI Justification Matrix:\n -> Decision: {explainable_payload['decision']}\n -> Justification: {explainable_payload['justification']}")
    assert explainable_payload["decision"] == "Strong Hire"

    # 3. Test GDPR 90-Day Purge Lifecycle Trigger
    stale_record = {
        "candidate_id": "USR-4091",
        "created_at": "2026-01-10",
        "masked_transcript": "highly fluent system programming conversation...",
        "final_score": 88
    }
    
    # Evaluate record simulating current date as June 8, 2026 (Exceeds 90 Days)
    purged_record = enforce_data_retention(stale_record, current_date_str="2026-06-08")
    print(f"\nData Retention Lifecycle (Simulating Expiry):")
    print(f" -> Current Status: {purged_record['status']}")
    print(f" -> Transcript State: {purged_record['masked_transcript']}")
    assert purged_record["masked_transcript"] == "[DATA_EXPUNGED]"
    
    print("\n✅ Day 43 Automated Ethical & Compliance Controls Verified Successfully.")

if __name__ == "__main__":
    test_ethical_pipeline()