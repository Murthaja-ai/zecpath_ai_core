import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.noise_handler import clean_noise
from screening_ai.robust_flow import detect_edge_case, handle_edge_case

def test_edge_cases():
    print("🧪 Running Test: Day 31 Chaos Engineering...")
    
    # 1. Test Noise Cleaner
    raw_text = "I am a [dog barks] backend developer"
    cleaned = clean_noise(raw_text)
    assert cleaned == "I am a backend developer", f"Regex failed, got: {cleaned}"
    print("   -> [Noise Handler]: Successfully stripped audio markers.")
    
    # 2. Test Hardware Confidence Drop
    poor_audio_result = detect_edge_case("I am a backend developer", confidence=0.4)
    assert poor_audio_result == "poor_audio", "Failed to detect poor audio."
    print("   -> [Edge Detector]: Successfully caught low-confidence hardware signal.")
    
    # 3. Test Code Switching
    mixed_text = "I am a developer pakshe backend aanu"
    lang_result = detect_edge_case(mixed_text, confidence=0.9)
    assert lang_result == "language_mix", "Failed to detect code-switching."
    print("   -> [Edge Detector]: Successfully caught language mixing.")
    
    # 4. Test Adaptive Router (Infinite Loop Protection)
    action = handle_edge_case("um", confidence=0.9, retry_count=2)
    assert action == "skip_question", "Failed to enforce safety fallback."
    print("   -> [Adaptive Router]: Safety fallback triggered correctly on retry limit.")
    
    print("\n✅ All Edge Case & Chaos tests passed!")

if __name__ == "__main__":
    test_edge_cases()