# security_core/governance_config.py

class GovernancePolicy:
    # Strict Data Retention Timers (in days)
    RETENTION_SCHEDULE = {
        "resume_data": 90,
        "interview_transcripts": 60,
        "reports_and_scores": 120,
        "audit_logs": 180
    }

    # Enterprise Role-Based Access Control (RBAC)
    # Notice we define exactly WHAT they can interact with, not just "read/write"
    ROLE_PERMISSIONS = {
        "admin": ["view_all", "delete_records", "export_audit_logs", "run_ai_pipeline"],
        "recruiter": ["view_assigned_candidates", "run_ai_pipeline"],
        "viewer": ["view_assigned_candidates"]
    }