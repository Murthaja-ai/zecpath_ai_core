import re
import os
import sys

# Ensure script can find the models folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from models.understanding_validator import UnderstoodAnswer
from screening_ai.intent_classifier import AnswerIntent

# --- Company Regex & Keyword Maps ---
INTENT_MAP = {
    "introduction": ["introduce", "about myself", "background"],
    "experience": ["experience", "years", "worked", "role"],
    "skills": ["skills", "technologies", "tools"],
    "salary": ["salary", "ctc", "pay"],
    "availability": ["notice period", "available", "join"]
}
SKILL_DB = ["python", "java", "django", "react", "sql", "angular"]

class AnswerUnderstandingEngine:
    def __init__(self):
        print("🧠 Booting up Rule-Based Answer Engine (with Pydantic Firewall)...")

    def _classify_intent(self, text: str) -> str:
        text_lower = text.lower()
        for intent, keywords in INTENT_MAP.items():
            for word in keywords:
                if word in text_lower:
                    return intent
        return "unknown"

    def _extract_skills(self, text: str) -> list:
        return [skill for skill in SKILL_DB if skill in text.lower()]

    def _extract_experience(self, text: str) -> int:
        match = re.search(r"(\d+)\s*(years|year)", text.lower())
        return int(match.group(1)) if match else 0

    def _extract_salary(self, text: str):
        match = re.search(r"(\d+)\s*(lpa|lakhs|k)", text.lower())
        return match.group(0) if match else None

    def _extract_availability(self, text: str) -> str:
        if "immediate" in text.lower(): return "Immediate"
        elif "notice" in text.lower(): return "Notice Period"
        return "Unknown"

    def process_answer(self, question_id: str, answer_text: str) -> dict:
        """Processes a single answer and pushes it through the validation firewall."""
        intent_val = self._classify_intent(answer_text)
        is_off_topic = (intent_val == "unknown")
        is_vague = any(word in answer_text.lower() for word in ["maybe", "not sure", "don't know"])
        is_missing = not answer_text or len(answer_text.strip()) < 3

        # Build raw dictionary using Company Logic
        structured = {
            "question_id": question_id,
            "original_text": answer_text,
            "intent": intent_val,
            "skills": self._extract_skills(answer_text),
            "experience_years": self._extract_experience(answer_text),
            "salary": self._extract_salary(answer_text),
            "availability": self._extract_availability(answer_text),
            "off_topic": is_off_topic,
            "is_vague": is_vague,
            "is_missing": is_missing
        }

        # Push it through the Pydantic Firewall!
        validated_data = UnderstoodAnswer(**structured)
        return validated_data.model_dump()

    def process_answers_batch(self, answers: list) -> list:
        """Processes a full list of candidate answers at once."""
        return [self.process_answer(ans["question_id"], ans["text"]) for ans in answers]

# --- Quick Test ---
if __name__ == "__main__":
    engine = AnswerUnderstandingEngine()
    result = engine.process_answer("Q3", "I have 3 years experience in Python and Django")
    import json
    print(json.dumps(result, indent=2))