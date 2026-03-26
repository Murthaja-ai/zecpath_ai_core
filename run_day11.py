import os
import json
from parsers.resume_parser import ResumeParser
from parsers.resume_segmenter import ResumeSegmenter
from parsers.education_parser import EducationParser

def run_education_pipeline():
    # 1. Setup Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_resume_dir = os.path.join(base_dir, "data", "raw_resumes")
    processed_dir = os.path.join(base_dir, "data", "processed")
    
    parser = ResumeParser()
    segmenter = ResumeSegmenter()
    edu_parser = EducationParser()

    # 2. Find the PDF dynamically (We are using sample_resume.pdf)
    pdf_files = [f for f in os.listdir(raw_resume_dir) if f.endswith('.pdf')]
    if not pdf_files:
        print("❌ No PDF found.")
        return
    
    target_file = pdf_files[0]
    pdf_path = os.path.join(raw_resume_dir, target_file)

    print(f"📄 Reading {target_file}...")
    raw_text = parser.extract_text(pdf_path)
    
    # 3. Segment the text (Isolate Education & Certifications)
    segmented_data = segmenter.segment(raw_text)
    
    edu_lines = segmented_data.get("EDUCATION", [])
    cert_lines = segmented_data.get("CERTIFICATIONS", [])
    
    # 4. Parse & Score Education
    print("🎓 Extracting and Normalizing Academic Profile...")
    parsed_education = edu_parser.parse_education(edu_lines) if edu_lines else []
    
    # 5. Parse Certifications
    print("📜 Tagging Certifications...")
    parsed_certs = edu_parser.parse_certifications(cert_lines) if cert_lines else []

    # 6. Build Final Enterprise Output
    final_output = {
        "candidate_file": target_file,
        "academic_profile": parsed_education,
        "certifications": parsed_certs
    }
    
    output_path = os.path.join(processed_dir, "education_extracted.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=4, ensure_ascii=False)

    print(f"\n✅ Success! Day 11 Education Engine complete.")
    print(f"📂 Saved Enterprise JSON to: {output_path}")

if __name__ == "__main__":
    run_education_pipeline()