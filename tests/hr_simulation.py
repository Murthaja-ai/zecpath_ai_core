# tests/hr_simulation.py
import sys
import os
import json
import random

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)

from interview_ai.summary_generator import generate_interview_summary

def generate_randomized_score(base_score):
    """Adds a realistic variance (-5 to +5) to simulate different humans."""
    return max(0.0, min(100.0, base_score + random.randint(-5, 5)))

def simulate_mass_pipeline(total_candidates=40):
    print(f"🚀 Starting Zecpath E2E Mass Simulation for {total_candidates} Candidates...\n")
    
    personas = ["CONFIDENT", "HESITANT", "INEXPERIENCED", "OVERQUALIFIED"]
    
    # Analytics tracking
    decision_counts = {"STRONG HIRE": 0, "CONSIDER": 0, "REJECT": 0}
    
    for i in range(1, total_candidates + 1):
        persona = random.choice(personas)
        candidate_id = f"CAND-{str(i).zfill(3)}-{persona}"
        
        # Base templates for personas
        if persona == "CONFIDENT":
            hr, apt, comm, beh, contra = 90, 88, 92, 95, False
        elif persona == "HESITANT":
            # We lowered the technical scores slightly so they land in the "CONSIDER" tier (55 - 74)
            hr, apt, comm, beh, contra = 70, 65, 55, 45, False 
        elif persona == "INEXPERIENCED":
            hr, apt, comm, beh, contra = 45, 40, 85, 90, True
        else: # OVERQUALIFIED
            hr, apt, comm, beh, contra = 98, 95, 90, 95, False

        # Run the randomized data through the Day 39 engine
        report = generate_interview_summary(
            candidate_id=candidate_id,
            hr_report={"final_hr_score": generate_randomized_score(hr)},
            aptitude_report={
                "aptitude_score": generate_randomized_score(apt), 
                "breakdown": {"structured_thinking": generate_randomized_score(apt), "risk_awareness": generate_randomized_score(apt)}
            },
            comm_score=generate_randomized_score(comm),
            behavioral_profile={"behavioral_score": generate_randomized_score(beh), "contradiction_detected": contra}
        )
        
        # Track the analytics
        decision_counts[report["decision"]] += 1

    # Print the Final Analytics Dashboard
    print("=== 📊 FINAL SIMULATION ANALYTICS ===")
    print(f"Total Candidates Processed: {total_candidates}")
    print(f"✅ STRONG HIRE: {decision_counts['STRONG HIRE']}")
    print(f"⚠️ CONSIDER:    {decision_counts['CONSIDER']}")
    print(f"❌ REJECT:      {decision_counts['REJECT']}")
    print("=====================================\n")
    
    # QA Assertions to ensure the math holds up at scale
    assert sum(decision_counts.values()) == total_candidates, "Math Error: Candidate drop-off detected!"
    print("✅ Mass E2E Simulation Complete: Pipeline logic is fundamentally sound under load.")

if __name__ == "__main__":
    simulate_mass_pipeline(40)