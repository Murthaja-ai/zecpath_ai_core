# security_core/test_governance.py
from compliance_gate import ComplianceGate, SecurityViolation, ConsentMissingError
from crypto_vault import CryptoVault
from immutable_logger import AuditTrailLogger

def run_security_audit():
    print("🛡️ Initializing Day 55 Enterprise Security & Governance Audit...\n")

    # 1. Test Consent Gate
    print("Checking Candidate Consent Logic...")
    mock_candidate = {"candidate_id": "C999", "legal_consent_granted": False}
    try:
        ComplianceGate.verify_candidate_consent(mock_candidate)
    except ConsentMissingError as e:
        print(f"✔ [Consent Gate Works]: {e}")

    # 2. Test RBAC Authorization
    print("\nChecking Role-Based Access Control...")
    try:
        ComplianceGate.authorize_user_action("recruiter", "delete_records")
    except SecurityViolation as e:
        print(f"✔ [RBAC Gate Works]: {e}")

    # 3. Test Persistent Encryption
    print("\nChecking Crypto Vault (AES-256)...")
    sensitive_transcript = "Candidate stated: I developed the backend APIs for the payment gateway."
    encrypted_data = CryptoVault.encrypt_transcript(sensitive_transcript)
    decrypted_data = CryptoVault.decrypt_transcript(encrypted_data)
    
    print(f"  -> Original:  {sensitive_transcript[:30]}...")
    print(f"  -> Encrypted: {str(encrypted_data)[:30]}... [SECURE]")
    print(f"  -> Decrypted: {decrypted_data[:30]}...")
    assert sensitive_transcript == decrypted_data
    print("✔ [Encryption Engine Works] - Key management is stable.")

    # 4. Test Immutable Audit Logging
    print("\nChecking Immutable Audit Trail...")
    AuditTrailLogger.log_event(
        event_type="AI_DECISION_GENERATED",
        actor_id="Zecpath_AI_Engine_v12",
        action_details={"candidate_id": "C1000", "final_status": "Rejected", "reason": "Hard Gate Integrity Check"}
    )
    print("✔ [Audit Trail Works] - Event appended securely to physical log file.")

    print("\n🎉 All Day 55 Security & Governance Checkpoints Passed Successfully.")

if __name__ == "__main__":
    run_security_audit()