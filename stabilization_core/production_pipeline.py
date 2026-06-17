# stabilization_core/production_pipeline.py
import sys
import os

# Link to our entire Zecpath architecture
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from security_core.compliance_gate import ComplianceGate, ConsentMissingError
from optimization_core.score_refiner import StatisticalScoreRefiner
from optimization_core.engine_tuner import OptimizedDecisionEngine
from stabilization_core.data_sanitizer import DataSanitizer
from stabilization_core.nlp_guard import NLPGuard
from stabilization_core.api_formatter import APIFormatter

# THE ATTACK: A corrupted candidate profile designed to crash basic systems
CORRUPTED_CANDIDATE = {
    "candidate_id": "P_999_CORRUPTED",
    "legal_consent_granted": True,
    "scores": {
        "ats": "N/A",        # String instead of float
        "screening": -50,    # Impossible negative number
        "hr": 150.5,         # Overflow number > 100
        "technical": None    # Missing data entirely
    },
    "integrity_status": "Low Risk",
    "voice_transcript": "   " # Blank space (Microphone error)
}

def execute_hardened_pipeline(candidate: dict):
    print(f"🛡️ Processing Candidate: {candidate['candidate_id']}")
    
    # THE MASTER SHOCK ABSORBER (Try/Except block prevents server death)
    try:
        # 1. Check Consent (Security)
        ComplianceGate.verify_candidate_consent(candidate)
        
        # 2. SANITIZE DATA (Day 57 Shield)
        print("  -> Raw Scores Detected. Engaging Sanitizer...")
        clean_scores = DataSanitizer.sanitize_score_dictionary(candidate["scores"])
        print(f"  -> Cleaned Scores: {clean_scores}")
        
        # 3. VERIFY TRANSCRIPT (Day 57 Shield)
        nlp_status = NLPGuard.evaluate_transcript_integrity(candidate["voice_transcript"])
        if nlp_status != "VALID_TRANSCRIPT":
             print(f"  -> NLP Guard Warning: {nlp_status}")
             # We adapt instead of crashing!
             clean_scores["screening"] = 0.0 
             
        # 4. Standard Math & Logic (Days 51-54)
        raw_values = list(clean_scores.values())
        base_score = sum(raw_values) / len(raw_values)
        refined_score = StatisticalScoreRefiner.generate_refined_score(clean_scores, base_score)
        
        engine = OptimizedDecisionEngine()
        decision = engine.evaluate_candidate_edge_cases(refined_score, clean_scores["technical"], candidate["integrity_status"])
        
        # 5. Return strict API format (Day 57 Shield)
        payload = {"candidate_id": candidate["candidate_id"], "final_score": refined_score, "decision": decision}
        return APIFormatter.build_response(success=True, data=payload)

    except Exception as e:
        # If ANYTHING goes catastrophically wrong, catch the explosion and return a safe error object.
        return APIFormatter.build_response(success=False, error_message=f"System Exception: {str(e)}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("🔥 INITIATING CHAOS TEST (DAY 57 HARDENING)")
    print("="*50)
    
    # Run the corrupted candidate through the hardened pipeline
    api_response = execute_hardened_pipeline(CORRUPTED_CANDIDATE)
    
    print("\n📡 FINAL API RESPONSE TO FRONTEND:")
    import json
    print(json.dumps(api_response, indent=2))