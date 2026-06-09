import json
from interview_ai.compliance_engine import mask_candidate_demographics, generate_explainable_output
from interview_ai.stability_optimizer import smooth_candidate_scores

# IMPORT FIXED: Using your exact Day 41 function name!
from interview_ai.unified_scoring_engine import generate_unified_profile

def execute_production_interview_pipeline(candidate_data: dict) -> dict:
    """The master execution loop for Phase 5. Processes transcripts, filters anomalies, and unifies scores."""
    
    # Step 1: Compliance Scrubbing (Blind the AI)
    clean_transcript = mask_candidate_demographics(
        raw_text=candidate_data["raw_transcript"], 
        candidate_name="John" # Simulated extraction
    )
    
    # Step 2: Stability & Outlier Smoothing
    stable_comm_score = smooth_candidate_scores(
        sub_scores=candidate_data["interview_metrics"]["communication_sub_scores"],
        confidence_score=candidate_data["interview_metrics"]["confidence_system_metric"]
    )
    
    # Step 3: Compile HR Matrix
    hr_aggregate = (stable_comm_score * 0.5) + (candidate_data["interview_metrics"]["aptitude_score"] * 0.5)
    
    # Step 4: The Grand Unifier (Using your actual function!)
    candidate_id = candidate_data.get("candidate_id", "UNKNOWN")
    profile = generate_unified_profile(
        candidate_id=candidate_id,
        candidate_type="technical", # Automatically applying your technical weights
        ats_score=candidate_data["historical_metrics"]["ats_score"],
        screening_score=candidate_data["historical_metrics"]["screening_score"],
        interview_score=hr_aggregate
    )
    
    final_score = profile["unified_hiring_score"]
    decision = profile["final_decision"].title() # Formats "STRONG HIRE" to "Strong Hire" for UI
    
    # Combine system vetoes with manual HR vetoes
    all_vetoes = candidate_data.get("active_vetoes", [])
    if profile.get("veto_flag"):
        all_vetoes.append(profile["veto_flag"])
        
    # Hard override for critical security/compliance violations
    if all_vetoes and any("SECURITY" in v for v in all_vetoes):
        final_score = 0.0
        decision = "Reject"

    # Step 5: Generate Legal Explainability
    final_report = generate_explainable_output(
        final_score=final_score,
        breakdowns={"ats": candidate_data["historical_metrics"]["ats_score"], "hr_aggregate": hr_aggregate},
        vetoes_triggered=all_vetoes
    )
    
    # Package for final dashboard output
    final_report["final_score"] = final_score
    final_report["decision"] = decision
    final_report["anonymized_transcript"] = clean_transcript
    
    return final_report

if __name__ == "__main__":
    with open("demo/hr_demo_dataset.json", "r") as file:
        dataset = json.load(file)
        print("\n=== ZECPATH AI CORE: LIVE PRODUCTION DEMO ===")
        for candidate in dataset:
            result = execute_production_interview_pipeline(candidate)
            print(f"\nCandidate ID: {candidate['candidate_id']}")
            print(f"Final Score: {result['final_score']}")
            print(f"Decision: {result['decision']}")
            
            # Safely grab the justification regardless of the dictionary key
            justification = result.get('justification', result.get('explanation', 'Rejected due to veto.'))
            print(f"Justification: {justification}")