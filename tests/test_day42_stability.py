# tests/test_day42_stability.py
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.stability_optimizer import optimize_transcript, smooth_candidate_scores, evaluate_followup_state

def test_stability_suite():
    print("=== Running Day 42 Stability Suite ===")
    
    # 1. Test Text Optimization & Data Extraction
    dirty_text = "I think, um, basically the architectural layer is, like, like, ready."
    clean_result = optimize_transcript(dirty_text)
    print(f"Raw Text: '{dirty_text}'")
    print(f"Cleaned:  '{clean_result['cleaned_text']}' | Fillers Extracted: {clean_result['filler_count']}")
    assert clean_result["filler_count"] == 4
    assert "like" not in clean_result["cleaned_text"]

    # 2. Test Outlier Anomaly Filter
    # Candidate scored highly, but one sub-evaluation hit 10.0 due to a simulated system fluke
    volatile_scores = [88.0, 92.0, 10.0, 85.0] 
    smoothed_metric = smooth_candidate_scores(volatile_scores, confidence_score=95.0)
    print(f"\nRaw Scores: {volatile_scores} | Smoothed & Bias-Adjusted Score: {smoothed_metric}")
    # The 10.0 should be excluded from processing, leaving an average around ~88, blended with 95 confidence
    assert smoothed_metric > 80.0

    # 3. Test Loop Protection
    loop_status = evaluate_followup_state("uncertain", retry_count=2)
    print(f"\nLoop State (Retry 2): {loop_status}")
    assert loop_status == "TERMINATE_LOOP_PROCEED_TO_NEXT_ROUND"
    
    print("\n✅ Day 42 System Stabilization Checks Complete.")

if __name__ == "__main__":
    test_stability_suite()