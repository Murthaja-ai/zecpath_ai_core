# stabilization_core/nlp_guard.py

class NLPGuard:
    @staticmethod
    def evaluate_transcript_integrity(transcript: str) -> str:
        """
        Checks if the transcript is healthy enough for the AI to analyze.
        Prevents NLP engines from crashing on null strings.
        """
        if not transcript or not isinstance(transcript, str):
            return "ERROR_EMPTY"
            
        cleaned = transcript.strip()
        word_count = len(cleaned.split())
        
        if word_count == 0:
            return "ERROR_EMPTY"
        if word_count < 3:
            return "ERROR_TOO_SHORT"
        if len(cleaned) > 2000:
            return "ERROR_TOO_LONG"
            
        return "VALID_TRANSCRIPT"