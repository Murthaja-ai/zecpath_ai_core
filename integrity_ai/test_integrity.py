# integrity_ai/test_integrity.py
from integrity_engine import IntegrityEngine
import json

def run_test():
    print("🛡️ Initializing Zecpath Security Shield...\n")
    engine = IntegrityEngine()

    # 1. We tell the AI the candidate is doing a complex architecture question
    current_interview_context = "system_design_challenge"

    # 2. We simulate the webcam/audio telemetry
    # The candidate is looking away a lot (10 times) AND the mic caught a voice (1 time)
    mock_telemetry = {
        "tab_switch": 0,
        "focus_loss": 0,
        "voice_detect": 1,
        "gaze_off": 10 
    }

    print(f"Active Context: {current_interview_context}")
    print(f"Incoming Telemetry: {mock_telemetry}\n")

    # 3. Process the data through our engine
    result = engine.assess_interview_integrity(mock_telemetry, current_interview_context)

    # 4. Print the final HR payload
    print("=== FINAL SECURITY REPORT ===")
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    run_test()