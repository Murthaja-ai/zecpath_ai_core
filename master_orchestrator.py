import os
import json
import csv
from parsers.semantic_engine import SemanticEngine
from parsers.scoring_engine import ScoringEngine

def stream_candidates(processed_folder):
    """
    ENTERPRISE GENERATOR (Day 18 Optimization)
    Yields one candidate at a time. Memory usage stays flat at 1% 
    instead of loading 10,000 files into a list.
    """
    if not os.path.exists(processed_folder):
        print(f"⚠️ Folder not found: {processed_folder}")
        return

    for filename in os.listdir(processed_folder):
        if filename.endswith(".json") and not filename.startswith('.'):
            file_path = os.path.join(processed_folder, filename)
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    candidate_data = json.load(f)
                    # The Magic Keyword: pauses the loop, sends the data, and frees the RAM
                    yield filename, candidate_data 
            except Exception as e:
                print(f"⚠️ Could not read {filename}: {e}")

def run_master_orchestrator():
    print("🚀 Booting up the Zecpath Master Orchestrator V3.1 (Generator Streaming)...")
    
    semantic_engine = SemanticEngine()
    scoring_engine = ScoringEngine()
    
    # 1. THE JOB DESCRIPTION
    jd_requirements = {
        "role": "Quantitative Analyst",
        "role_level": "mid_level",
        "required_skills": ["Python", "Machine Learning", "Statistical Modeling", "SQL", "Data Visualization"],
    }
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    processed_folder = os.path.join(base_dir, "data", "processed")
    results_file = os.path.join(base_dir, "data", "final_ats_scores.csv")
    
    print("\n⚙️ Streaming candidates from disk using Python Generators...")
    
    # Open a CSV file to stream our results into
    with open(results_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["Filename", "Final_Score", "Matched_Skills", "Missing_Skills"])
        
        count = 0
        # 2. THE PIPELINE LOOP (Consumes the generator one by one)
        for filename, candidate_data in stream_candidates(processed_folder):
            count += 1
            
            # Extract skills from the JSON the parser made
            candidate_skills = candidate_data.get("skills", [])
            
            # (In a fully connected pipeline, these would come from your other engines)
            candidate_exp_score = 0.85 
            candidate_project_score = 0.78
            edu_score = 0.5
            
            # 3. SEMANTIC GAP ANALYSIS
            skill_analysis = semantic_engine.analyze_skill_gap(candidate_skills, jd_requirements["required_skills"])
            
            # 4. PREPARE RAW SCORES
            raw_scores = {
                "skills": skill_analysis["score"],
                "experience": candidate_exp_score,
                "projects": candidate_project_score,
                "education": edu_score
            }
            
            # 5. DYNAMIC SCORING
            scoring_result = scoring_engine.calculate_final_score(jd_requirements["role_level"], raw_scores)
            
            final_score_percent = round(scoring_result['final_score'] * 100, 1)
            
            # 6. STREAM TO DISK (Save result, immediately forget candidate to free RAM)
            writer.writerow([
                filename, 
                final_score_percent,
                ", ".join(skill_analysis['matched']),
                ", ".join(skill_analysis['missing'])
            ])
            print(f"✅ Scored {filename} -> {final_score_percent}%")

    print(f"\n🏁 Finished processing {count} candidates with 0% memory bloat!")
    print(f"📁 Enterprise Report saved to: {results_file}")

if __name__ == "__main__":
    run_master_orchestrator()