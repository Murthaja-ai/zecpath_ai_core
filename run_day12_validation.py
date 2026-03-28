import os
import json
from parsers.semantic_engine import SemanticEngine

def generate_accuracy_report():
    print("🚀 Booting up Day 12 Validation Engine...")
    engine = SemanticEngine()
    
    # 1. DEFINE MULTIPLE JDs (To prove the AI knows the difference)
    jds = [
        {
            "id": "JD_001",
            "role": "Quantitative Analyst",
            "required_skills": ["Python", "Machine Learning", "Statistical Modeling", "SQL", "Data Visualization"],
            "responsibilities": "Develop predictive models, analyze financial datasets, and build data pipelines using Python and SQL."
        },
        {
            "id": "JD_002",
            "role": "React Front-End Developer",
            "required_skills": ["JavaScript", "React", "CSS", "HTML", "UI/UX Design"],
            "responsibilities": "Build responsive web interfaces, design user components with React, and ensure cross-browser CSS compatibility."
        }
    ]
    
    # 2. DEFINE CANDIDATE DATA (Including raw text for Projects & Experience)
    # This simulates the raw text extracted by your parsers in Days 8 and 10
    candidate = {
        "id": "CAND_001",
        "skills": ["Python 3", "Deep Neural Networks", "Pandas", "PostgreSQL", "Tableau"],
        "experience_text": "Worked as a Data Analyst. Built ETL pipelines using PostgreSQL and Python. Analyzed large datasets to find market trends.",
        "project_text": "Trained a Deep Neural Network to predict housing prices. Visualized the outputs using Tableau dashboards."
    }
    
    # 3. RUN THE VALIDATION MATRICES
    print("\n🧠 Scanning candidate against multiple JDs...")
    report_results = []
    
    for jd in jds:
        print(f"   -> Analyzing match for: {jd['role']}...")
        
        # A. Skill Gap
        skill_analysis = engine.analyze_skill_gap(candidate["skills"], jd["required_skills"])
        
        # B. Experience Semantic Match (Checking text vs text)
        exp_match = engine.calculate_similarity(candidate["experience_text"], jd["responsibilities"])
        
        # C. Project Semantic Match (Checking text vs text)
        proj_match = engine.calculate_similarity(candidate["project_text"], jd["responsibilities"])
        
        # D. Calculate Final Composite Score
        # Weights: Skills (50%), Experience (30%), Projects (20%)
        composite_score = (skill_analysis["score"] * 0.50) + (exp_match * 0.30) + (proj_match * 0.20)
        
        # E. Determine Recommendation
        if composite_score >= 0.55:
            recommendation = "Strong Match — Shortlist"
        elif composite_score >= 0.35:
            recommendation = "Moderate Match — Consider"
        else:
            recommendation = "Poor Match — Reject"
            
        report_results.append({
            "jd_id": jd["id"],
            "jd_role": jd["role"],
            "candidate_id": candidate["id"],
            "scores": {
                "skill_match": round(skill_analysis["score"], 3),
                "experience_match": exp_match,
                "project_match": proj_match,
                "composite_score": round(composite_score, 3)
            },
            "skill_gap": {
                "matched": skill_analysis["matched"],
                "missing": skill_analysis["missing"]
            },
            "recommendation": recommendation
        })
        
    # 4. EXPORT THE ACCURACY REPORT
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "processed")
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, "matching_accuracy_report.json")
    
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report_results, f, indent=4)
        
    print("\n" + "="*60)
    print("✅ DAY 12 COMPLETE: MATCHING ACCURACY REPORT GENERATED")
    print("="*60)
    print(f"📁 Saved to: {report_path}")
    
    # Print a quick summary to terminal
    for res in report_results:
        print(f"\nRole: {res['jd_role']}")
        print(f"-> Final Score: {res['scores']['composite_score'] * 100:.1f}% | {res['recommendation']}")

if __name__ == "__main__":
    generate_accuracy_report()