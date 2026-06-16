# simulation_core/persona_dataset.py

# A curated dataset of candidate personas designed to trigger every security gate and optimization curve.
CANDIDATE_PERSONAS = [
    {
        "candidate_id": "P_001",
        "persona_name": "The Perfect Hire",
        "legal_consent_granted": True,
        "scores": {"ats": 88.0, "screening": 85.0, "hr": 89.0, "technical": 92.0},
        "integrity_status": "Low Risk",
        "voice_transcript": "I developed the cloud architecture for the backend system."
    },
    {
        "candidate_id": "P_002",
        "persona_name": "The Brilliant Cheater",
        "legal_consent_granted": True,
        "scores": {"ats": 98.0, "screening": 95.0, "hr": 99.0, "technical": 100.0},
        "integrity_status": "High Risk", # Should trigger Day 54 & Day 55 Hard Gates
        "voice_transcript": "I built the entire database."
    },
    {
        "candidate_id": "P_003",
        "persona_name": "The Volatile Genius",
        "legal_consent_granted": True,
        "scores": {"ats": 90.0, "screening": 60.0, "hr": 40.0, "technical": 99.0}, # Huge Variance
        "integrity_status": "Low Risk",
        "voice_transcript": "I plan to optimize the data pipeline."
    },
    {
        "candidate_id": "P_004",
        "persona_name": "The Unconsented User",
        "legal_consent_granted": False, # Should trigger Day 55 Crash
        "scores": {"ats": 85.0, "screening": 80.0, "hr": 85.0, "technical": 88.0},
        "integrity_status": "Low Risk",
        "voice_transcript": "I learned Python in college."
    }
]