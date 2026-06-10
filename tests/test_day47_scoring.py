# tests/test_day47_scoring.py
from technical_ai.evaluation_engine import TechnicalScoringEngine
from technical_ai.report_generator import TechnicalReportGenerator

def test_technical_scoring_pipeline():
    """Validates the Day 47 Scoring Engine and Report Generator."""
    
    engine = TechnicalScoringEngine()
    generator = TechnicalReportGenerator()

    # --- Test 1: A Deep, Senior-Level Answer ---
    deep_answer = "I would prioritize the system architecture first, because under the hood, the memory tradeoff is absolutely critical for maintaining scalable performance in a high-traffic production scenario."
    eval_deep = engine.process_answer(
        answer=deep_answer, 
        question_type="system_design", 
        difficulty="advanced", 
        is_correct=True
    )
    
    # Assert the engine successfully detected a deep answer and rewarded it
    assert eval_deep["depth_classification"] == "deep"
    assert eval_deep["final_normalized_score"] > 80.0

    # --- Test 2: A Shallow, Junior-Level Answer ---
    shallow_answer = "I think you just use a database."
    eval_shallow = engine.process_answer(
        answer=shallow_answer, 
        question_type="conceptual", 
        difficulty="basic", 
        is_correct=False
    )
    
    # Assert the engine punished the shallow, incorrect answer
    assert eval_shallow["depth_classification"] == "shallow"
    assert eval_shallow["final_normalized_score"] < 50.0

    # --- Test 3: The Report Generator ---
    # Simulate the end of the interview by compiling the history
    session_history = [
        {"question_id": "Q1", "skill_domain": "System Architecture", "evaluation": eval_deep},
        {"question_id": "Q2", "skill_domain": "Database Logic", "evaluation": eval_shallow}
    ]

    report = generator.generate_final_report("C-500", session_history)

    # Assert the final HR report compiled correctly
    assert report["candidate_id"] == "C-500"
    assert "overall_technical_score" in report
    assert len(report["detailed_question_breakdown"]) == 2