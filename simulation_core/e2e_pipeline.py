# simulation_core/e2e_pipeline.py
import sys
import os
import time

# This allows our simulation to "see" the folders we built on Day 54 and Day 55
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from security_core.compliance_gate import ComplianceGate, ConsentMissingError
from security_core.crypto_vault import CryptoVault
from security_core.immutable_logger import AuditTrailLogger
from optimization_core.score_refiner import StatisticalScoreRefiner
from optimization_core.engine_tuner import OptimizedDecisionEngine
from persona_dataset import CANDIDATE_PERSONAS

def run_full_system_simulation():
    print("="*60)
    print("🚀 ZECPATH END-TO-END (E2E) SYSTEM SIMULATION INITIALIZED")
    print("="*60 + "\n")
    
    engine = OptimizedDecisionEngine()
    simulation_results = []

    for candidate in CANDIDATE_PERSONAS:
        print(f"🔄 Processing: {candidate['candidate_id']} ({candidate['persona_name']})")
        start_time = time.time()
        
        try:
            # STEP 1: SECURITY CORE - Check Consent (Day 55)
            ComplianceGate.verify_candidate_consent(candidate)
            
            # STEP 2: AGGREGATION CORE - Calculate Base Score
            raw_scores = [float(v) for v in candidate["scores"].values()]
            base_score = sum(raw_scores) / len(raw_scores)
            
            # STEP 3: OPTIMIZATION CORE - Apply Standard Deviation (Day 54)
            refined_score = StatisticalScoreRefiner.generate_refined_score(candidate["scores"], base_score)
            
            # STEP 4: DECISION CORE - Evaluate Hard Gates & Edge Cases (Day 54)
            final_decision = engine.evaluate_candidate_edge_cases(
                refined_score=refined_score, 
                technical_score=candidate["scores"]["technical"], 
                integrity_status=candidate["integrity_status"]
            )
            
            # STEP 5: SECURITY CORE - Encrypt Transcripts & Log Audit (Day 55)
            encrypted_transcript = CryptoVault.encrypt_transcript(candidate["voice_transcript"])
            AuditTrailLogger.log_event(
                event_type="E2E_EVALUATION_COMPLETE",
                actor_id="Zecpath_Master_Pipeline",
                action_details={"candidate_id": candidate["candidate_id"], "final_decision": final_decision}
            )
            
            processing_time = round((time.time() - start_time) * 1000, 2)
            
            print(f"  [+] Base Score: {base_score:.1f}% | Refined Score: {refined_score:.1f}%")
            print(f"  [+] Final Decision: {final_decision.upper()}")
            print(f"  [+] Execution Time: {processing_time}ms | Transcript Encrypted: YES\n")
            
        except ConsentMissingError as e:
            # Catches the Unconsented User
            print(f"  [-] FATAL ERROR: {str(e)}\n")
            AuditTrailLogger.log_event("E2E_EVALUATION_BLOCKED", "Zecpath_Master_Pipeline", {"candidate_id": candidate["candidate_id"], "reason": "No Consent"})

if __name__ == "__main__":
    run_full_system_simulation()