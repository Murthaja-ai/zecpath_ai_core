import os
import json
from parsers.resume_parser import ResumeParser
from parsers.resume_segmenter import ResumeSegmenter

def run_segmentation_pipeline():
    # 1. Setup Paths
    base_dir = os.path.dirname(os.path.abspath(__file__))
    raw_resume_dir = os.path.join(base_dir, "data", "raw_resumes")
    processed_dir = os.path.join(base_dir, "data", "processed")
    
    # Ensure processed directory exists
    os.makedirs(processed_dir, exist_ok=True)

    # 2. Initialize our Tools
    parser = ResumeParser()       # The Reader (Day 4)
    segmenter = ResumeSegmenter() # The Organizer (Day 8)

    # 3. Find a PDF to process
    # We look for ANY pdf in the folder
    pdf_files = [f for f in os.listdir(raw_resume_dir) if f.endswith('.pdf')]
    
    if not pdf_files:
        print("❌ No PDF found in data/raw_resumes/")
        print("👉 Please put 'fake_resume_murthaja.pdf' in that folder!")
        return

    # Let's process the first one found
    target_file = pdf_files[0]
    pdf_path = os.path.join(raw_resume_dir, target_file)
    print(f"📄 Processing: {target_file}...")

    # 4. Step A: Extract Raw Text (Day 4 Logic)
    # We toggle 'full=True' if your parser supports it, otherwise it just returns text
    raw_text = parser.extract_text(pdf_path)
    
    # 5. Step B: Segment the Text (Day 8 Logic)
    print("🧠 AI is identifying sections...")
    segmented_data = segmenter.segment(raw_text)

    # 6. Step C: Save the Result
    output_filename = target_file.replace(".pdf", "_segmented.json")
    output_path = os.path.join(processed_dir, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(segmented_data, f, indent=4)

    print(f"✅ Success! Segmented data saved to: {output_path}")
    
    # 7. Print a sneak peek
    print("\n--- 🔍 Segmented Preview ---")
    print(f"Name/Summary: {segmented_data['SUMMARY'][:2]}") # Show first 2 lines
    print(f"Experience:   {len(segmented_data['EXPERIENCE'])} lines found")
    print(f"Education:    {len(segmented_data['EDUCATION'])} lines found")
    print(f"Skills:       {len(segmented_data['SKILLS'])} lines found")

if __name__ == "__main__":
    run_segmentation_pipeline()