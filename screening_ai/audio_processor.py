import speech_recognition as sr
import os
import sys

# Import our Day 23 Normalizer to clean the text immediately!
from screening_ai.transcript_normalizer import normalize_transcript

class SpeechToTextEngine:
    def __init__(self):
        print("🎧 Booting up Speech-to-Text Engine...")
        self.recognizer = sr.Recognizer()
        
        # --- DAY 24 REQUIREMENT: SILENCE DETECTION & NOISE ---
        # These settings tell the AI how to handle background noise and pauses
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.energy_threshold = 300  # Baseline for background noise
        self.recognizer.pause_threshold = 2.0   # Wait 2 full seconds of silence before cutting off
        self.recognizer.non_speaking_duration = 0.5 # Handle small stutters

    def transcribe_audio_file(self, file_path: str) -> dict:
        """
        Ingests an audio file, converts it to text, and cleans it.
        """
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}"}

        print(f"🎙️ Analyzing audio file: {file_path}")
        
        # Load the audio file into memory
        with sr.AudioFile(file_path) as source:
            # Calibrate for ambient background noise (Day 24 requirement)
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen to the entire file
            audio_data = self.recognizer.record(source)

        try:
            # Using Google's free STT for local testing. 
            # In production, we swap this one line to recognize_whisper()
            print("⏳ Transcribing via STT Engine...")
            raw_text = self.recognizer.recognize_google(audio_data)
            
            # --- DAY 24 REQUIREMENT: TEXT CLEANUP ---
            # Pass the raw text directly into our Day 23 Washing Machine!
            clean_text = normalize_transcript(raw_text)

            return {
                "status": "success",
                "raw_audio_text": raw_text,
                "normalized_text": clean_text,
                "confidence_estimated": 0.92 # Placeholder for Google Web API
            }

        except sr.UnknownValueError:
            return {"status": "failed", "error": "AI could not understand the audio (too much noise or silence)."}
        except sr.RequestError as e:
            return {"status": "failed", "error": f"API Error: {e}"}

# --- Quick Test ---
if __name__ == "__main__":
    engine = SpeechToTextEngine()
    print("✅ Audio Engine is ready to listen!")