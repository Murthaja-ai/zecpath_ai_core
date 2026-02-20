import fitz  # PyMuPDF for PDF
import docx  # python-docx for Word
import re
import spacy
import json
import os
import csv
from text_cleaner import clean_text  # Import your new helper

# Load AI Model
nlp = spacy.load("en_core_web_sm")

def load_skills():
    """Loads skill database from JSON"""
    try:
        # Go up one level to find data/skill_patterns.json
        path = os.path.join(os.path.dirname(__file__), '..', 'data', 'skill_patterns.json')
        with open(path, 'r') as f:
            data = json.load(f)
        
        # Flatten the list (we just want a big list of words to search for)
        flat_skills = []
        for category, skills in data.items():
            flat_skills.extend(skills)
        return flat_skills
    except FileNotFoundError:
        print("⚠️ Warning: skill_patterns.json not found. Using empty list.")
        return []

# Load skills ONCE when the script starts
SKILLS_DB = load_skills()

def extract_text_from_pdf(path):
    try:
        doc = fitz.open(path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error reading PDF {path}: {e}")
        return ""

def extract_text_from_docx(path):
    try:
        doc = docx.Document(path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    except Exception as e:
        print(f"Error reading DOCX {path}: {e}")
        return ""

def parse_resume(file_path):
    """
    Main Logic: Detect Type -> Extract -> Clean -> Analyze
    """
    filename = os.path.basename(file_path)
    
    # 1. Detect File Type & Extract Raw Text
    if filename.endswith(".pdf"):
        raw_text = extract_text_from_pdf(file_path)
    elif filename.endswith(".docx"):
        raw_text = extract_text_from_docx(file_path)
    else:
        return None  # Skip images or other files

    # 2. Clean the Text (Using your text_cleaner.py)
    cleaned_text = clean_text(raw_text)

    # 3. Initialize Data Structure
    data = {
        "filename": filename,
        "email": None,
        "phone": None,
        "name": None,
        "skills": []
    }

    # 4. Extract Contact Info (Regex)
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', cleaned_text)
    if email_match:
        data["email"] = email_match.group(0)

    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\d{10})', cleaned_text)
    if phone_match:
        data["phone"] = phone_match.group(0).strip()

    # 5. Extract Name (AI with Filter)
    doc = nlp(cleaned_text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            # FILTER 1: Clean the text and remove anything after a newline
            # OLD LINE: name_candidate = ent.text.strip()
            # NEW LINE (The Fix):
            name_candidate = ent.text.strip().split('\n')[0]
            
            # FILTER 2: Is it a skill? (e.g., "Python")
            if name_candidate in SKILLS_DB:
                continue
            
            # FILTER 3: Is it a resume header?
            if name_candidate.lower() in ["resume", "curriculum vitae", "profile", "bio"]:
                continue
                
            # If it passes checks, accept it as the name
            data["name"] = name_candidate
            break
    # Fallback: If AI fails, take the very first line of the file (usually the name)
    if not data["name"]:
        first_line = cleaned_text.split('\n')[0].strip()
        # Ensure it's not an email or phone
        if "@" not in first_line and len(first_line) < 50:
             data["name"] = first_line

    # 6. Extract Skills (Keyword Matching against DB)
    # We use 'set' to avoid duplicates (e.g. finding "Python" twice)
    found_skills = set()
    for skill in SKILLS_DB:
        # \b ensures we match "Java" but not "JavaScript" when looking for Java
        pattern = r'\b' + re.escape(skill) + r'\b'
        if re.search(pattern, cleaned_text, re.IGNORECASE):
            found_skills.add(skill)
            
    data["skills"] = list(found_skills)

    return data

if __name__ == "__main__":
    # Define Paths
    base_dir = os.path.dirname(os.path.dirname(__file__)) # Go up to project root
    input_folder = os.path.join(base_dir, "data", "raw_resumes")
    output_folder = os.path.join(base_dir, "data", "processed")
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # CSV Log File for Reporting
    log_file = os.path.join(output_folder, "parsing_report.csv")
    
    print(f"🚀 Zecpath Parser V2 Starting...")
    print(f"📂 Reading from: {input_folder}")
    
    with open(log_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header Row
        writer.writerow(["Filename", "Status", "Name", "Email", "Skill Count"])

        # Loop through all files
        if os.path.exists(input_folder):
            for filename in os.listdir(input_folder):
                if filename.endswith((".pdf", ".docx")):
                    file_path = os.path.join(input_folder, filename)
                    
                    print(f"Processing: {filename}...")
                    result = parse_resume(file_path)
                    
                    if result:
                        # Success!
                        # 1. Save JSON
                        json_name = filename.rsplit('.', 1)[0] + ".json"
                        with open(os.path.join(output_folder, json_name), 'w') as jf:
                            json.dump(result, jf, indent=4)
                        
                        # 2. Log to CSV
                        writer.writerow([filename, "SUCCESS", result['name'], result['email'], len(result['skills'])])
                    else:
                        # Failure (Empty file or error)
                        writer.writerow([filename, "FAILED", "", "", 0])
        else:
            print("❌ Error: 'data/raw_resumes' folder not found.")

    print(f"\n✅ Done! Check the 'data/processed' folder for results.")