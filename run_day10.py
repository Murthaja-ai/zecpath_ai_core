import os
import json
from parsers.resume_parser import ResumeParser
from parsers.resume_segmenter import ResumeSegmenter
from parsers.experience_parser import ExperienceParser
from parsers.relevance_engine import RelevanceEngine

def run_experience_pipeline():
    # 1. Setup Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_resume_dir = os.path.join(base_dir, "data", "raw_resumes")
    processed_dir = os.path.join(base_dir, "data", "processed")
    
    parser = ResumeParser()
    segmenter = ResumeSegmenter()
    exp_parser = ExperienceParser()
    rel_engine = RelevanceEngine()
    
    # 2. Define the Zecpath Finance Target
    TARGET_ROLE = "Quantitative Equity Analyst"
    REQUIRED_YEARS = 3.0

    # 3. Find the PDF dynamically
    pdf_files = [f for f in os.listdir(raw_resume_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print("❌ No PDF found in raw_resumes folder.")
        return
    
    target_file = pdf_files[0]
    pdf_path = os.path.join(raw_resume_dir, target_file)

    print(f"📄 Reading {target_file}...")
    raw_text = parser.extract_text(pdf_path)
    
    # 4. Segment the text to isolate Experience
    segmented_data = segmenter.segment(raw_text)
    experience_text = "\n".join(segmented_data.get("EXPERIENCE", []))
    
    if not experience_text.strip():
        print("⚠️ No Experience section found in this resume.")
        return

    # 5. Extract timeline logic
    print("🧠 Extracting Job History & Analyzing Timeline...")
    parsed_experience = exp_parser.parse_experience(experience_text)
    
    # 6. Apply Relevance Scoring
    print(f"⚖️ Calculating Relevance against Employer Requirements...")
    relevance_scores = rel_engine.calculate_relevance(
        parsed_experience, 
        TARGET_ROLE, 
        REQUIRED_YEARS
    )

    # 7. Compile Final Output
    final_output = {
        "candidate_file": target_file,
        "total_experience_years": parsed_experience["total_experience_years"],
        "effective_relevant_years": relevance_scores["effective_relevant_years"],
        "experience_entries": parsed_experience["experience_entries"],
        "employment_gaps": parsed_experience["employment_gaps"]
    }
    
    output_path = os.path.join(processed_dir, "experience_scored.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=4)

    print(f"\n✅ Success! Experience V2 Engine complete.")
    print(f"📂 Saved Enterprise JSON to: {output_path}")

if __name__ == "__main__":
    run_experience_pipeline()