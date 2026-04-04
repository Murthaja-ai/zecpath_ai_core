from utils.anti_cheat import IntegrityChecker

def test_anti_cheat():
    checker = IntegrityChecker()
    
    print("\n" + "="*50)
    print(" DAY 15: ANTI-CHEAT SECURITY TEST")
    print("="*50 + "\n")
    
    # Candidate 1: An honest candidate
    honest_resume = "I am a software engineer with 4 years of experience. I build web applications."
    honest_skills = ["software engineer", "web applications"]
    
    # Candidate 2: A cheater (Pasted a block of invisible buzzwords)
    cheater_resume = "Python Java C++ SQL AWS Docker Kubernetes React Angular Vue Machine Learning Deep Learning Pandas Numpy Excel Agile Scrum"
    cheater_skills = ["Python", "Java", "C++", "SQL", "AWS", "Docker", "Kubernetes", "React", "Angular", "Vue", "Machine Learning", "Deep Learning", "Pandas", "Numpy", "Excel", "Agile", "Scrum"]

    # Run the checks
    print("--- 1. TESTING HONEST CANDIDATE ---")
    honest_result = checker.analyze_resume_integrity(honest_resume, honest_skills)
    print(f"Status: {honest_result['status']}")
    print(f"Reason: {honest_result['reason']}\n")
    
    print("--- 2. TESTING KEYWORD STUFFER ---")
    cheater_result = checker.analyze_resume_integrity(cheater_resume, cheater_skills)
    print(f"Status: {cheater_result['status']}")
    print(f"Reason: {cheater_result['reason']}")
    if cheater_result['penalty'] > 0:
        print(f"⚠️ APPLYING SYSTEM PENALTY: -{cheater_result['penalty']*100}% to Final Score")

if __name__ == "__main__":
    test_anti_cheat()