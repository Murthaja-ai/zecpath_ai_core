import os
import sys
from datetime import datetime, timezone

# This allows our test script to find the 'models' folder at the root
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from models.transcript_validator import TranscriptSession
from pydantic import ValidationError

def test_transcript_validation():
    print("🚀 Booting up Day 23 Transcript Validation Test...\n")

    # ---------------------------------------------------------
    # CASE 1: The Perfect Transcript
    # ---------------------------------------------------------
    print("Testing Case 1: Valid AI Transcript...")
    valid_data = {
        "session_id": "session_999",
        "metadata": {
            "candidate_id": "cand_001",
            "job_id": "job_frontend_01",
            "interview_date": datetime.now(timezone.utc).isoformat(),
            "language_detected": "en",
            "overall_audio_quality": "good"
        },
        "normalization_rules_applied": {
            "remove_filler_words": True,
            "lowercase_conversion": True,
            "punctuation_stripped": True
        },
        "dialogue_turns": [
            {
                "turn_id": 1,
                "speaker": "Candidate",
                "raw_text": "Uhh, yeah, I know Angular.",
                "normalized_text": "i know angular",
                "confidence_level": 0.95, # 95% confidence (Valid)
                "timestamp": datetime.now(timezone.utc).isoformat(), # This line was the culprit!
                "flagged_for_review": False
            }
        ],
        "session_status": "completed"
    }

    try:
        # We pass the dictionary into the Pydantic Enforcer
        validated_session = TranscriptSession(**valid_data)
        print("✅ Success! The Enforcer accepted the perfect transcript.")
    except ValidationError as e:
        print(f"❌ Failed: {e}")

    # ---------------------------------------------------------
    # CASE 2: The Broken Transcript
    # ---------------------------------------------------------
    print("\nTesting Case 2: Broken AI Transcript (Audio Engine Glitch)...")
    
    broken_data = valid_data.copy()
    # Deliberately break the rules: Confidence level cannot be higher than 1.0
    broken_data["dialogue_turns"][0]["confidence_level"] = 5.5 

    try:
        # We are TRYING to force the bad data into the model
        TranscriptSession(**broken_data)
        print("❌ Uh oh! The Enforcer failed and let bad data through!")
    except ValidationError as e:
        print("🛡️ BLOCKED! The Enforcer successfully caught the bad data:")
        print(f"   Reason: {e.errors()[0]['msg']}")

if __name__ == "__main__":
    test_transcript_validation()