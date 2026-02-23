import os
import re
import json
from text_cleaner import clean_text  # Reusing your Day 5 Janitor!

def load_skill_synonyms():
    """Loads our new Synonym Dictionary."""
    # CHANGED: Now points to synonyms_db.json to protect Day 5!
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'synonyms_db.json')
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ synonyms_db.json missing!")
        return {}

def extract_experience(text):
    """Finds min and max years of experience."""
    match = re.search(r'(\d+)(?:\s*-\s*(\d+))?\s*(?:\+)?\s*years?', text, re.IGNORECASE)
    if match:
        return {
            "min_years": int(match.group(1)),
            "max_years": int(match.group(2)) if match.group(2) else None
        }
    return {"min_years": 0, "max_years": None}

def extract_education(text):
    """Detects degree requirements."""
    text_lower = text.lower()
    if re.search(r"\b(master's|master|m\.s\.|ms)\b", text_lower):
        return "Master's Degree"
    elif re.search(r"\b(bachelor's|bachelor|b\.s\.|bs|btech|b\.tech)\b", text_lower):
        return "Bachelor's Degree"
    return "Not Specified"

def extract_skills(text, synonym_dict):
    """Uses the Synonym Engine to find skills in a block of text."""
    found_skills = set()
    for official_skill, synonyms in synonym_dict.items():
        for synonym in synonyms:
            # \b ensures exact word matches (e.g., finding "ML" but not "HTML")
            pattern = r'\b' + re.escape(synonym) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.add(official_skill)
                break  # If we find "ML", we don't need to keep searching for "Machine Learning"
    return list(found_skills)

def parse_jd(file_path):
    """Master Engine to process the Job Description."""
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()

    # 1. Clean the text (Remove weird formatting)
    cleaned_text = clean_text(raw_text)
    synonym_dict = load_skill_synonyms()

    # 2. Extract Basic Info
    jd_data = {
        "job_title": None,
        "requirements": {
            "experience": extract_experience(cleaned_text),
            "education": extract_education(cleaned_text),
            "mandatory_skills": [],
            "nice_to_have_skills": []
        }
    }

    title_match = re.search(r'Job Title:\s*(.*)', cleaned_text, re.IGNORECASE)
    if title_match:
        jd_data["job_title"] = title_match.group(1).strip()

    # 3. Split Text & Extract Skills
    lower_text = cleaned_text.lower()
    if "nice to have" in lower_text:
        parts = re.split(r'nice to have:?', cleaned_text, flags=re.IGNORECASE)
        mandatory_text = parts[0]
        nice_to_have_text = parts[1]
    else:
        mandatory_text = cleaned_text
        nice_to_have_text = ""

    # Pass the split text to our Synonym Engine!
    jd_data["requirements"]["mandatory_skills"] = extract_skills(mandatory_text, synonym_dict)
    jd_data["requirements"]["nice_to_have_skills"] = extract_skills(nice_to_have_text, synonym_dict)

    return jd_data

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_dir = os.path.join(base_dir, "data", "raw_jds")
    processed_dir = os.path.join(base_dir, "data", "processed")
    
    print("🚀 Starting Batch Job Description Parsing...\n")
    
    # Loop through every file in the raw_jds folder
    for filename in os.listdir(raw_dir):
        if filename.endswith(".txt"):
            jd_path = os.path.join(raw_dir, filename)
            
            # Create a new output filename (e.g., jd_data_engineer_parsed.json)
            output_filename = filename.replace(".txt", "_parsed.json")
            output_path = os.path.join(processed_dir, output_filename)
            
            # Parse and Save
            result = parse_jd(jd_path)
            with open(output_path, 'w') as f:
                json.dump(result, f, indent=4)
                
            print(f"✅ Successfully processed: {filename} -> {output_filename}")
            
    print("\n🎉 Batch processing complete! Check your data/processed/ folder.")