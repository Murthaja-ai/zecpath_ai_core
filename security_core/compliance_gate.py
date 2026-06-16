# security_core/compliance_gate.py
from governance_config import GovernancePolicy

class SecurityViolation(Exception):
    """Custom exception triggered during unauthorized access."""
    pass

class ConsentMissingError(Exception):
    """Custom exception triggered if AI runs on an unconsented profile."""
    pass

class ComplianceGate:
    @staticmethod
    def verify_candidate_consent(candidate_profile: dict):
        """HARD GATE: AI pipeline cannot legally execute without explicit consent."""
        consent_status = candidate_profile.get("legal_consent_granted", False)
        if not consent_status:
            raise ConsentMissingError(f"CRITICAL: Candidate {candidate_profile.get('candidate_id')} has NOT provided explicit data processing consent. AI Execution Blocked.")
        return True

    @staticmethod
    def authorize_user_action(user_role: str, requested_action: str):
        """Verifies if the current user has the legal clearance to perform an action."""
        allowed_actions = GovernancePolicy.ROLE_PERMISSIONS.get(user_role.lower(), [])
        
        if requested_action not in allowed_actions:
            raise SecurityViolation(f"ACCESS DENIED: Role '{user_role}' lacks authorization to execute '{requested_action}'.")
        return True