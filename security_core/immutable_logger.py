# security_core/immutable_logger.py
import json
import datetime
import os

class AuditTrailLogger:
    LOG_FILE = "security_core/system_audit.jsonl"

    @classmethod
    def log_event(cls, event_type: str, actor_id: str, action_details: dict):
        """
        Appends a secure, timestamped record to the audit trail.
        Uses JSON Lines (.jsonl) format to prevent historical data mutation.
        """
        audit_record = {
            "timestamp_utc": datetime.datetime.utcnow().isoformat(),
            "event_type": event_type,
            "actor_id": actor_id, # Could be User ID or "SYSTEM_AI"
            "details": action_details
        }
        
        # 'a' mode ensures we only append to the file, never overwrite it.
        with open(cls.LOG_FILE, "a") as file:
            file.write(json.dumps(audit_record) + "\n")
        
        return audit_record