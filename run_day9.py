import os
import json
from parsers.resume_parser import ResumeParser
from parsers.skill_extractor import SkillExtractor
from parsers.resume_segmenter import ResumeSegmenter

def run_skill_pipeline():
    # 1. Setup paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_resume_dir = os.path.join(base_dir, "data", "raw_resumes")
    processed_dir = os.path.join(base_dir, "data", "processed")
    db_path = os.path.join(base_dir, "data", "skills_db.json")
    
    parser = ResumeParser()
    extractor = SkillExtractor()
    
    # 2. Load the DB here just to know the categories (Tech vs Soft Skills)
    with open(db_path, "r", encoding="utf-8") as f:
        skill_db = json.load(f)
        
    # Create a quick dictionary to look up a skill's category
    category_map = {}
    for skill in skill_db:
        category_map[skill["name"]] = skill.get("category", "Technical")
        # Also map the inferred skills to the same category
        for related in skill.get("related_skills", []):
            category_map[related] = skill.get("category", "Technical")

    # 3. Find PDF
    pdf_files = [f for f in os.listdir(raw_resume_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print("❌ No PDF found.")
        return

    target_file = pdf_files[0]
    print(f"📄 Processing: {target_file}...")

    # 4. Extract Text
    raw_text = parser.extract_text(os.path.join(raw_resume_dir, target_file))
    
    # 4.5. SEGMENT THE TEXT FIRST (Day 8 Integration!)
    segmenter = ResumeSegmenter()
    segmented_data = segmenter.segment(raw_text)
    
    # Combine only the highly relevant buckets into one string
    targeted_text = "\n".join(
        segmented_data.get("SKILLS", []) + 
        segmented_data.get("EXPERIENCE", []) + 
        segmented_data.get("PROJECTS", [])
    )

    print("🧠 AI is identifying and structuring skills from targeted sections...")
    # Feed ONLY the targeted text to the extractor, not the whole PDF!
    extracted_skills = extractor.extract_skills(targeted_text)
    
    # --- 5. ENTERPRISE FORMATTING LOGIC ---
    structured_output = {
        "technical_skills": [],
        "business_skills": [],
        "soft_skills": []
    }

    for skill_name, score in extracted_skills.items():
        # Convert 100 -> 1.0, 90 -> 0.9, 50 -> 0.5
        confidence_decimal = round(score / 100.0, 2)
        
        # Get category from our map (default to Technical if unknown)
        raw_cat = category_map.get(skill_name, "Technical").lower()
        
        skill_entry = {"skill": skill_name, "confidence": confidence_decimal}
        
        # Sort into the correct bucket
        if "soft" in raw_cat:
            structured_output["soft_skills"].append(skill_entry)
        elif "business" in raw_cat or "management" in raw_cat:
            structured_output["business_skills"].append(skill_entry)
        else:
            structured_output["technical_skills"].append(skill_entry)

    # Sort each list so the highest confidence skills appear at the top
    for key in structured_output:
        structured_output[key] = sorted(structured_output[key], key=lambda x: x['confidence'], reverse=True)

    # 6. Save the final payload
    final_data = {
        "filename": target_file,
        "total_skills_found": len(extracted_skills),
        "extracted_skills": structured_output
    }
    
    output_path = os.path.join(processed_dir, "skills_extracted.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=4)

    print(f"✅ Success! Categorized {len(extracted_skills)} skills.")
    print(f"📂 Saved Enterprise JSON to: {output_path}")

if __name__ == "__main__":
    run_skill_pipeline()