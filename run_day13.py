from parsers.scoring_engine import ScoringEngine

def test_scoring_engine():
    scorer = ScoringEngine()
    
    print("\n" + "="*50)
    print("TEST 1: JUNIOR ROLE (Normal Data)")
    print("="*50)
    # A Junior dev with good college grades and projects, but low experience
    junior_scores = {"skills": 0.80, "experience": 0.20, "projects": 0.90, "education": 0.85}
    junior_result = scorer.calculate_final_score("junior", junior_scores)
    print(f"Final Score: {junior_result['final_score'] * 100:.1f}%")
    print(f"Audit Notes: {junior_result['audit_notes']}")
    
    print("\n" + "="*50)
    print("TEST 2: SENIOR ROLE (Missing Education Section!)")
    print("="*50)
    # A Senior dev with amazing experience, but their parser couldn't find an education section (None)
    senior_scores = {"skills": 0.90, "experience": 0.95, "projects": 0.60, "education": None}
    senior_result = scorer.calculate_final_score("senior", senior_scores)
    print(f"Final Score: {senior_result['final_score'] * 100:.1f}%")
    print("Effective Weights Used:", senior_result['effective_weights'])
    print("Audit Notes:")
    for note in senior_result['audit_notes']:
        print(f" - {note}")

if __name__ == "__main__":
    test_scoring_engine()