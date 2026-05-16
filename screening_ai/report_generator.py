def generate_screening_report(candidate_id, job_id, answers, scores, behavior_reports):
    strengths = []
    risks = []
    missing = []
    key_answers = []
    salary = "Not Disclosed"
    availability = "Unknown"
    confirmed_skills = set()

    for ans, score, behavior in zip(answers, scores, behavior_reports):
        # Key Answers Summary
        key_answers.append({
            "question_id": ans.get("question_id", "Unknown"),
            "answer": ans.get("original_text", "[No Answer]")
        })
        
        # Strengths
        if score.get("final_score", 0) >= 80:
            strengths.append(f"Strong answer in {ans.get('question_id')}")
            
        # Risks
        if score.get("final_score", 0) < 50 or behavior.get("communication_strength") == "Weak":
            risks.append(f"Weak response in {ans.get('question_id')}")
            
        # Missing Data
        if ans.get("is_vague") or ans.get("off_topic"):
            missing.append(f"Incomplete answer in {ans.get('question_id')}")
            
        # Extract highlights
        if ans.get("salary"):
            salary = ans["salary"]
        if ans.get("availability") and ans.get("availability") != "Unknown":
            availability = ans["availability"]
        for skill in ans.get("skills", []):
            confirmed_skills.add(skill)

    # Calculate final decision
    final_score = sum(s.get("final_score", 0) for s in scores) / len(scores) if scores else 0
    decision = "Proceed" if final_score >= 70 else "Review" if final_score >= 50 else "Reject"

    return {
        "candidate_id": candidate_id,
        "job_id": job_id,
        "final_score": round(final_score, 2),
        "decision": decision,
        "summary": {
            "strengths": strengths,
            "risks": risks,
            "missing_data": missing
        },
        "highlights": {
            "salary_expectation": salary,
            "availability": availability,
            "confirmed_skills": list(confirmed_skills)
        },
        "answers": key_answers
    }

# --- Quick Test ---
if __name__ == "__main__":
    ans_mock = [{"question_id": "Q1", "original_text": "I want 150k.", "salary": "150k", "skills": ["Python"]}]
    score_mock = [{"final_score": 85}]
    behav_mock = [{"communication_strength": "Strong"}]
    
    report = generate_screening_report("C123", "J101", ans_mock, score_mock, behav_mock)
    import json
    print(json.dumps(report, indent=2))