from parsers.semantic_engine import SemanticEngine

def test_semantic_matching():
    engine = SemanticEngine()
    
    # ---------------------------------------------------------
    # TEST 1: The Keyword Problem
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("TEST 1: SINGLE CONCEPT MATCHING")
    print("="*50)
    
    jd_requirement = "Machine Learning"
    
    candidate_exact = "Machine Learning"
    candidate_semantic = "Deep Neural Networks"
    candidate_bad = "Interior Design"
    
    print(f"JD Wants: '{jd_requirement}'")
    print(f" -> Resume has '{candidate_exact}' | Score: {engine.calculate_similarity(jd_requirement, candidate_exact)}")
    print(f" -> Resume has '{candidate_semantic}' | Score: {engine.calculate_similarity(jd_requirement, candidate_semantic)}")
    print(f" -> Resume has '{candidate_bad}'      | Score: {engine.calculate_similarity(jd_requirement, candidate_bad)}")
    
    
    # ---------------------------------------------------------
    # TEST 2: Full Skill Profile Comparison
    # ---------------------------------------------------------
    print("\n" + "="*50)
    print("TEST 2: FULL CANDIDATE PROFILE MATCHING")
    print("="*50)
    
    jd_skills = ["Python", "Data Analysis", "Cloud Computing"]
    print(f"Target JD Skills: {jd_skills}\n")
    
    # Candidate 1 has the skills, but wrote them differently
    candidate_1_skills = ["Pandas and NumPy", "AWS Architecture", "Python 3"]
    score_1 = engine.match_skill_lists(candidate_1_skills, jd_skills)
    
    # Candidate 2 is in a totally different industry
    candidate_2_skills = ["Adobe Photoshop", "Social Media Marketing", "Copywriting"]
    score_2 = engine.match_skill_lists(candidate_2_skills, jd_skills)
    
    print(f"Candidate 1 (Tech) Skills: {candidate_1_skills}")
    print(f"✅ Candidate 1 Match Score: {score_1 * 100:.1f}%\n")
    
    print(f"Candidate 2 (Marketing) Skills: {candidate_2_skills}")
    print(f"❌ Candidate 2 Match Score: {score_2 * 100:.1f}%")

if __name__ == "__main__":
    test_semantic_matching()