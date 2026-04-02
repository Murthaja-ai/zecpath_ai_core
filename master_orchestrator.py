import os
import json
from parsers.semantic_engine import SemanticEngine
from parsers.scoring_engine import ScoringEngine

def run_master_orchestrator():
    print("🚀 Booting up the Zecpath Master Orchestrator V3.0 (Dynamic Scoring)...")
    
    # Initialize our two powerful AI engines
    semantic_engine = SemanticEngine()
    scoring_engine = ScoringEngine()
    
    # 1. THE JOB DESCRIPTION
    jd_requirements = {
        "role": "Quantitative Analyst",
        "role_level": "mid_level", # We now define the seniority for dynamic weighting!
        "required_skills": ["Python", "Machine Learning", "Statistical Modeling", "SQL", "Data Visualization"],
    }
    
    # 2. LOAD CANDIDATE DATA
    candidate_exp_years = 4.5
    candidate_exp_score = 0.85 
    candidate_project_score = 0.78 # Simulating a project match score
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    edu_file_path = os.path.join(base_dir, "data", "processed", "education_extracted.json")
    
    if os.path.exists(edu_file_path):
        with open(edu_file_path, "r", encoding="utf-8") as f:
            candidate_data = json.load(f)
    else:
        candidate_data = {"academic_profile": [{"education_relevance_score": 0.5}]}

    edu_score = candidate_data.get("academic_profile", [{}])[0].get("education_relevance_score", 0.5)
    candidate_skills = ["Python 3", "Deep Neural Networks", "Pandas", "PostgreSQL", "Tableau"]
    
    # 3. SEMANTIC GAP ANALYSIS
    print("\n🧠 Performing Semantic Skill Gap Analysis...")
    skill_analysis = semantic_engine.analyze_skill_gap(candidate_skills, jd_requirements["required_skills"])
    
    # 4. PREPARE RAW SCORES FOR THE SCORING ENGINE
    raw_scores = {
        "skills": skill_analysis["score"],
        "experience": candidate_exp_score,
        "projects": candidate_project_score,
        "education": edu_score
    }
    
    # 5. DYNAMIC SCORING (No more hardcoded math!)
    print("⚖️ Applying Dynamic Role-Based Weights...")
    scoring_result = scoring_engine.calculate_final_score(jd_requirements["role_level"], raw_scores)
    
    # 6. ENTERPRISE OUTPUT REPORT
    print("\n" + "="*60)
    print("📊 ZECPATH ATS: OFFICIAL CANDIDATE SCORECARD (V3.0)")
    print("="*60)
    print(f"Target Role : {jd_requirements['role']} ({jd_requirements['role_level'].upper()})")
    print("-" * 60)
    
    print("🛠️  SKILL GAP ANALYSIS")
    print(f"   ✅ Matched : {', '.join(skill_analysis['matched']) if skill_analysis['matched'] else 'None'}")
    print(f"   ❌ Missing : {', '.join(skill_analysis['missing']) if skill_analysis['missing'] else 'None'}")
    print("-" * 60)
    
    print("⚖️  SCORING BREAKDOWN & AUDIT TRAIL")
    for category, weight in scoring_result["effective_weights"].items():
        raw_val = raw_scores.get(category, 0)
        print(f"   -> {category.capitalize():<12} | Raw: {raw_val*100:>5.1f}% | Weight: {weight*100:>4.1f}%")
        
    if scoring_result["audit_notes"]:
        print("\n   [SYSTEM AUDIT NOTES]:")
        for note in scoring_result["audit_notes"]:
            print(f"   ! {note}")
            
    print("="*60)
    print(f"🏆 FINAL ENTERPRISE MATCH SCORE: {scoring_result['final_score'] * 100:.1f}%")
    print("="*60)

if __name__ == "__main__":
    run_master_orchestrator()