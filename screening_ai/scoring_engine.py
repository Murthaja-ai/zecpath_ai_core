import os
import sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from models.scoring_validator import QuestionScore, FinalScreeningScore, SubScores, Explanations, SummaryAverages
from models.understanding_validator import UnderstoodAnswer

# --- Company Scoring Weights ---
WEIGHTS = {
    "clarity": 0.25,
    "relevance": 0.30,
    "completeness": 0.25,
    "consistency": 0.20
}

class ScreeningScoringEngine:
    def __init__(self):
        print("⚖️ Booting up Screening Scoring Engine (Weighted MVP)...")

    def _score_clarity(self, answer: UnderstoodAnswer) -> tuple[float, str]:
        text = answer.original_text
        length = len(text.split()) if text else 0
        if length > 8: return 1.0, "Answer is detailed and well-structured."
        elif length > 4: return 0.7, "Answer is adequately clear but brief."
        elif length > 1: return 0.4, "Answer lacks detail and clarity."
        return 0.0, "Answer is missing or extremely short."

    def _score_relevance(self, answer: UnderstoodAnswer, expected_intent: str) -> tuple[float, str]:
        if answer.intent.value == expected_intent:
            return 1.0, f"Matches expected intent ({expected_intent})."
        return 0.3, f"Intent mismatch. Expected {expected_intent}, got {answer.intent.value}."

    def _score_completeness(self, answer: UnderstoodAnswer) -> tuple[float, str]:
        score = 0.0
        reasons = []
        if answer.skills:
            score += 0.4
            reasons.append("Includes skills")
        if answer.experience_years > 0:
            score += 0.3
            reasons.append("Includes experience")
        if answer.availability != "Unknown":
            score += 0.3
            reasons.append("Includes availability")
        
        final_score = min(score, 1.0)
        expl = " and ".join(reasons) if reasons else "Missing key extracted data."
        return final_score, expl

    def _score_consistency(self, answer: UnderstoodAnswer) -> tuple[float, str]:
        if answer.is_vague: return 0.3, "Vague language detected."
        if answer.off_topic: return 0.2, "Off-topic indicator triggered."
        return 1.0, "No vague or off-topic indicators."

    def score_answer(self, answer: UnderstoodAnswer, expected_intent: str) -> QuestionScore:
        c_score, c_expl = self._score_clarity(answer)
        r_score, r_expl = self._score_relevance(answer, expected_intent)
        comp_score, comp_expl = self._score_completeness(answer)
        cons_score, cons_expl = self._score_consistency(answer)

        final = (
            (c_score * WEIGHTS["clarity"]) +
            (r_score * WEIGHTS["relevance"]) +
            (comp_score * WEIGHTS["completeness"]) +
            (cons_score * WEIGHTS["consistency"])
        )

        structured_data = {
            "question_id": answer.question_id,
            "scores": {
                "clarity": round(c_score, 2),
                "relevance": round(r_score, 2),
                "completeness": round(comp_score, 2),
                "consistency": round(cons_score, 2)
            },
            "final_score": round(final * 100, 2),
            "explanation": {
                "clarity": c_expl,
                "relevance": r_expl,
                "completeness": comp_expl,
                "consistency": cons_expl
            }
        }
        return QuestionScore(**structured_data)

    def screening_scoring_pipeline(self, candidate_id: str, answers: list[UnderstoodAnswer], intent_map: dict) -> FinalScreeningScore:
        scored_answers = []
        for ans in answers:
            expected = intent_map.get(ans.question_id, "unknown")
            scored_answers.append(self.score_answer(ans, expected))

        if not scored_answers:
            # Return empty fail state
            summary = SummaryAverages(avg_clarity=0, avg_relevance=0, avg_completeness=0, avg_consistency=0)
            return FinalScreeningScore(candidate_id=candidate_id, screening_score=0.0, decision="Reject", breakdown=[], summary=summary)

        total = sum(a.final_score for a in scored_answers)
        avg_score = round(total / len(scored_answers), 2)
        
        # Company Decision Rules
        decision = "Pass" if avg_score >= 70 else "Review" if avg_score >= 50 else "Reject"

        # Calculate Summary Averages
        avg_c = round(sum(a.scores.clarity for a in scored_answers) / len(scored_answers), 2)
        avg_r = round(sum(a.scores.relevance for a in scored_answers) / len(scored_answers), 2)
        avg_comp = round(sum(a.scores.completeness for a in scored_answers) / len(scored_answers), 2)
        avg_cons = round(sum(a.scores.consistency for a in scored_answers) / len(scored_answers), 2)

        summary = {
            "avg_clarity": avg_c, "avg_relevance": avg_r,
            "avg_completeness": avg_comp, "avg_consistency": avg_cons
        }

        return FinalScreeningScore(
            candidate_id=candidate_id,
            screening_score=avg_score,
            decision=decision,
            breakdown=scored_answers,
            summary=summary
        )

# --- Quick Test ---
if __name__ == "__main__":
    from screening_ai.intent_classifier import AnswerIntent
    engine = ScreeningScoringEngine()
    
    test_ans = UnderstoodAnswer(
        question_id="Q3",
        original_text="I have 3 years experience in Python",
        intent=AnswerIntent.EXPERIENCE,
        skills=["python"],
        experience_years=3,
        availability="Immediate",
        off_topic=False,
        is_vague=False,
        is_missing=False
    )

    intent_map = {"Q3": "experience"}
    result = engine.screening_scoring_pipeline("C123", [test_ans], intent_map)
    print(result.model_dump_json(indent=2))