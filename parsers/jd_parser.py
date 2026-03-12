import os
import re
import json
from text_cleaner import clean_text

def load_skill_synonyms():
    path = os.path.join(os.path.dirname(__file__), '..', 'data', 'synonyms_db.json')
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ synonyms_db.json missing!")
        return {}

def extract_experience(text):
    match = re.search(r'(\d+)(?:\s*-\s*(\d+))?\s*(?:\+)?\s*years?', text, re.IGNORECASE)
    if match:
        return {
            "min_years": int(match.group(1)),
            "max_years": int(match.group(2)) if match.group(2) else None
        }
    return {"min_years": 0, "max_years": None}

def extract_education(text):
    text_lower = text.lower()
    degrees = []
    
    if re.search(r"\b(mba|master's|master|m\.s\.|ms)\b", text_lower):
        degrees.append("MBA/Master's")
    if re.search(r"\b(cfa)\b", text_lower):
        degrees.append("CFA")
    if re.search(r"\b(ca)\b", text_lower):
        degrees.append("CA")
    if re.search(r"\b(bachelor's|bachelor|b\.s\.|bs|bcom|degree in finance)\b", text_lower):
        degrees.append("Bachelor's/Degree in Finance")
        
    return ", ".join(degrees) if degrees else "Not Specified"

def extract_skills(text, synonym_dict):
    found_skills = set()
    for official_skill, synonyms in synonym_dict.items():
        for synonym in synonyms:
            pattern = r'\b' + re.escape(synonym) + r'\b'
            if re.search(pattern, text, re.IGNORECASE):
                found_skills.add(official_skill)
                break 
    return list(found_skills)

def parse_jd(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    cleaned_text = clean_text(raw_text)
    synonym_dict = load_skill_synonyms()
    
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
        
    lower_text = cleaned_text.lower()
    if "nice to have" in lower_text:
        parts = re.split(r'nice to have:?', cleaned_text, flags=re.IGNORECASE)
        mandatory_text = parts[0]
        nice_to_have_text = parts[1]
    else:
        mandatory_text = cleaned_text
        nice_to_have_text = ""
        
    jd_data["requirements"]["mandatory_skills"] = extract_skills(mandatory_text, synonym_dict)
    jd_data["requirements"]["nice_to_have_skills"] = extract_skills(nice_to_have_text, synonym_dict)
    
    return jd_data

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(__file__))
    raw_dir = os.path.join(base_dir, "data", "raw_jds")
    processed_dir = os.path.join(base_dir, "data", "processed")    
    
    print("🚀 Starting Batch Job Description Parsing...\n")
    master_database = []
    
    # --- THE CLEANING CREW ---
    for filename in os.listdir(processed_dir):
        if filename.endswith("_parsed.json"):
            os.remove(os.path.join(processed_dir, filename))
            
    # --- THE SORTER (New Step) ---
    # Get all text files and sort them mathematically by the role number in the filename
    files = [f for f in os.listdir(raw_dir) if f.endswith(".txt")]
    
    def get_role_number(filename):
        match = re.search(r'role_(\d+)', filename)
        return int(match.group(1)) if match else 999
        
    files.sort(key=get_role_number)
            
    # --- PROCESS ALL FILES IN EXACT NUMERICAL ORDER ---
    for filename in files:
        jd_path = os.path.join(raw_dir, filename)
        result = parse_jd(jd_path)
        master_database.append(result)
        print(f"✅ Processed: {filename}")        
            
    # --- SAVE MASTER DATABASE ---
    output_path = os.path.join(processed_dir, "master_jobs_db.json")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_database, f, indent=4)      
          
    print(f"\n🎉 Success! Compiling {len(master_database)} jobs in perfect numerical order!")