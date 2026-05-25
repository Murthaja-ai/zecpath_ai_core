# interview_ai/state_tracker.py
import sys
import os
import json

# --- PATH FIX ---
# Calculate the absolute path to the root 'zecpath_ai_core' folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base_dir not in sys.path:
    sys.path.append(base_dir)
# ----------------

from interview_ai.followup_engine import detect_answer_quality, generate_followup
from interview_ai.adaptive_engine import adapt_question_level, generate_adaptive_question

class InterviewState:
    def __init__(self):
        self.history = []
        self.asked_questions = set()
        
    def add_interaction(self, question: str, answer: str):
        self.history.append({
            "question": question,
            "answer": answer
        })
        self.asked_questions.add(question)
        
    def is_repeated(self, question: str) -> bool:
        return question in self.asked_questions

def avoid_repetition(state: InterviewState, question_pool: list) -> list:
    """Filters out any questions that have already been asked."""
    return [q for q in question_pool if not state.is_repeated(q)]

def followup_pipeline(current_question: str, current_answer: str, next_planned_question: str, confidence_score: float):
    """The Master Pipeline: Evaluates current answer, triggers follow-ups, and adapts the next question."""
    quality = detect_answer_quality(current_answer)
    
    # Step 1: Generate follow-up if the current answer was bad
    followup = generate_followup(current_question, quality)
    
    # Step 2: Adapt the difficulty of the NEXT question based on current performance
    mode = adapt_question_level(quality, confidence_score)
    adaptive_next_question = generate_adaptive_question(next_planned_question, mode)
    
    return {
        "quality_detected": quality,
        "immediate_followup": followup,
        "adapted_next_question": adaptive_next_question
    }

if __name__ == "__main__":
    # Test the full pipeline exactly as the company requested
    print("=== Testing Adaptive Pipeline ===")
    result = followup_pipeline(
        current_question="Tell me about your teamwork experience.",
        current_answer="I worked in a team.", # 5 words -> Basic Quality
        next_planned_question="How do you resolve conflicts?",
        confidence_score=0.6
    )
    
    print(json.dumps(result, indent=4))