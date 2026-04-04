import hashlib

class DataAnonymizer:
    def __init__(self):
        print("🛡️ Booting up PII Anonymizer (Blind Hiring Module)...")

    def mask_identity(self, candidate_name):
        """
        Creates a consistent, irreversible short-hash for a candidate.
        Example: 'Alice (The Expert)' -> 'Candidate_F3A1'
        """
        # Create a secure hash of the candidate's string
        hash_object = hashlib.sha256(candidate_name.encode('utf-8'))
        
        # Take just the first 4 characters of the hex digest and make them uppercase
        short_hash = hash_object.hexdigest()[:4].upper()
        
        return f"Candidate_{short_hash}"

    def anonymize_profile(self, candidate_data):
        """
        Takes a candidate dictionary and strips/masks identifying info.
        """
        anonymized_data = candidate_data.copy()
        
        # 1. Mask the name
        original_name = anonymized_data.get("candidate_name", "Unknown")
        masked_name = self.mask_identity(original_name)
        anonymized_data["candidate_name"] = masked_name
        
        # 2. Strip other potential PII (Personally Identifiable Information)
        # Upgraded to comply with global GDPR and Equal Opportunity laws
        pii_keys = [
            "email", "phone", "linkedin", "address", 
            "gender", "age", "dob", "marital_status", 
            "nationality", "religion", "photo"
        ]
        for key in pii_keys:
            if key in anonymized_data:
                del anonymized_data[key]
                
        return anonymized_data