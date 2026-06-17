# stabilization_core/data_sanitizer.py

class DataSanitizer:
    @staticmethod
    def clean_score(raw_value) -> float:
        """
        Safely converts any input into a valid float.
        Clamps the final number strictly between 0.0 and 100.0.
        """
        if raw_value is None:
            return 0.0
            
        try:
            # Attempt to convert strings like "85.5" to a float
            float_val = float(raw_value)
        except (ValueError, TypeError):
            # If it's pure garbage text like "N/A" or a corrupted object
            return 0.0
            
        # The Clamp: Forces negative numbers to 0, and numbers > 100 down to 100
        clamped_val = max(0.0, min(float_val, 100.0))
        return round(clamped_val, 2)

    @staticmethod
    def sanitize_score_dictionary(scores: dict) -> dict:
        """Cleans an entire dictionary of candidate scores instantly."""
        return {key: DataSanitizer.clean_score(val) for key, val in scores.items()}