# observability_core/immutable_audit.py
import hashlib
import json
from datetime import datetime, timezone

class ImmutableAuditVault:
    def __init__(self):
        # In production, this would be a secure database table
        self.ledger = []
        self.previous_hash = "GENESIS_BLOCK_0000"

    def record_decision(self, candidate_id: str, decision: str, scores: dict):
        """Creates a cryptographically secure audit trail for legal defense."""
        
        audit_record = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "candidate_id": candidate_id,
            "final_decision": decision,
            "score_snapshot": scores,
            "previous_hash": self.previous_hash
        }
        
        # 1. Convert the dictionary to a strict JSON string
        record_string = json.dumps(audit_record, sort_keys=True).encode('utf-8')
        
        # 2. Generate a SHA-256 Cryptographic Hash
        current_hash = hashlib.sha256(record_string).hexdigest()
        audit_record["cryptographic_hash"] = current_hash
        
        # 3. Save to Ledger and update chain
        self.ledger.append(audit_record)
        self.previous_hash = current_hash
        
        print(f"🔒 [AUDIT VAULT] Immutable Record Created for {candidate_id}")
        print(f"   Hash Signature: {current_hash[:16]}...\n")
        return audit_record

if __name__ == "__main__":
    print("\n🏛️ TESTING CRYPTOGRAPHIC AUDIT VAULT")
    vault = ImmutableAuditVault()
    
    # Simulating final hiring decisions
    vault.record_decision("C_001", "Selected", {"tech": 95, "hr": 88})
    vault.record_decision("C_002", "Rejected", {"tech": 40, "hr": 60})
    
    print("Full Ledger State (Ready for Legal Audit):")
    print(json.dumps(vault.ledger, indent=2))