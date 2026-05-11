import os
import sys

# Ensure our script can find the screening_ai folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.audio_processor import SpeechToTextEngine

def test_audio_pipeline():
    print("🚀 Booting up Day 24 Audio Pipeline Test...\n")
    
    # 1. Locate the test audio file
    audio_path = os.path.join(base_dir, "data", "audio_samples", "test_audio.wav")
    
    if not os.path.exists(audio_path):
        print(f"❌ Error: Could not find the audio file at {audio_path}")
        print("Please make sure you recorded 'test_audio.wav' and placed it in data/audio_samples/")
        return

    # 2. Spin up the engine
    stt_engine = SpeechToTextEngine()
    
    # 3. Process the file
    print(f"\n🎧 Feeding audio to the AI...")
    result = stt_engine.transcribe_audio_file(audio_path)
    
    # 4. Display the magical results
    if result.get("status") == "success":
        print("\n✅ AI Successfully Transcribed the Audio!")
        print("-" * 50)
        print(f"🗣️ Raw Audio Text : '{result['raw_audio_text']}'")
        print(f"✨ Cleaned Text   : '{result['normalized_text']}'")
        print(f"🎯 Confidence     : {result['confidence_estimated']}")
        print("-" * 50)
    else:
        print(f"\n❌ AI Failed to process audio: {result.get('error')}")

if __name__ == "__main__":
    test_audio_pipeline()