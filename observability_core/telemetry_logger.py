# observability_core/telemetry_logger.py
import json
import uuid
import re
from datetime import datetime, timezone

class PIIMasker:
    """Detects and masks sensitive candidate data before it is logged."""
    EMAIL_REGEX = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    PHONE_REGEX = r'\+?\d{1,3}?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'

    @staticmethod
    def mask_data(text: str) -> str:
        if not isinstance(text, str):
            return text
        text = re.sub(PIIMasker.EMAIL_REGEX, '[MASKED_EMAIL]', text)
        text = re.sub(PIIMasker.PHONE_REGEX, '[MASKED_PHONE]', text)
        return text

class ZecpathTelemetry:
    """Enterprise Logger with Correlation IDs and PII Masking."""
    
    @staticmethod
    def log_event(level: str, service: str, event_type: str, data: dict, correlation_id: str = None):
        if not correlation_id:
            correlation_id = f"req_{uuid.uuid4().hex[:8]}"
            
        # Deep mask the data dictionary
        safe_data = {k: PIIMasker.mask_data(str(v)) for k, v in data.items()}
        
        log_entry = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "level": level.upper(),
            "correlation_id": correlation_id,
            "service": service,
            "event": event_type,
            "safe_payload": safe_data
        }
        
        # In a real app, this writes to Datadog, Splunk, or AWS CloudWatch
        print(json.dumps(log_entry, indent=2))
        return correlation_id

if __name__ == "__main__":
    print("\n🛡️ TESTING PII-SAFE TELEMETRY LOGGER")
    logger = ZecpathTelemetry()
    
    # Simulating a frontend request containing sensitive data
    unsafe_payload = {
        "candidate_name": "John Doe",
        "contact_email": "john.doe.genius@gmail.com",
        "contact_phone": "+1-555-019-8372",
        "ats_score": 92.5
    }
    
    print("\nIncoming Unsafe Data Triggered...")
    logger.log_event(
        level="INFO",
        service="ATS_Service",
        event_type="resume_parsed",
        data=unsafe_payload
    )