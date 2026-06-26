# core/final_polish.py
import json
from statistics import stdev

class ZecpathProductionPolish:
    def __init__(self):
        self.version = "v1.0-PRODUCTION"

    # PATCH B: Recalibrated Variance Engine (Day 64 Audit)
    def calculate_final_score(self, scores: dict) -> float:
        values = list(scores.values())
        if not values: return 0.0
        
        avg = sum(values) / len(values)
        # Tuned down from 0.4 to 0.15 to prevent false negatives for top talent
        variance_penalty = stdev(values) * 0.15 if len(values) > 1 else 0 
        
        return round(max(0, avg - variance_penalty), 2)

    # PATCH C: Graceful Error Handling for ATS
    def parse_resume_safely(self, file_payload: dict) -> dict:
        try:
            if file_payload.get('is_flattened_image'):
                # Graceful degradation instead of a silent crash
                return {
                    "success": False,
                    "http_status": 415,
                    "error_code": "UNSUPPORTED_MEDIA_TYPE",
                    "user_message": "We detected an image-based PDF (e.g., Canva export). Please upload a standard text PDF for AI parsing."
                }
            return {"success": True, "http_status": 200, "text": "[Parsed Resume Data]"}
            
        except KeyError as e:
            # Catching specific errors, avoiding blanket 'except Exception'
            return {"success": False, "http_status": 400, "error": f"Missing required field: {str(e)}"}