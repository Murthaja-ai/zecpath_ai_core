import fitz  # PyMuPDF for PDF
import docx  # python-docx for Word
import re
import spacy
import json
import os
import csv
import concurrent.futures  # <-- NEW: Added for parallel processing
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
            name_candidate = ent.text.strip().split('\n')[0]
            
            # --- NEW DAY 18 FILTER: Refine Entity Detection ---
            # Reject the name if it contains numbers or is absurdly long
            if any(char.isdigit() for char in name_candidate) or len(name_candidate) > 30:
                continue
            # --------------------------------------------------
            
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

def process_single_file(file_path, output_folder):
    """
    Helper function designed to be run in parallel.
    Processes one file, saves the JSON, and returns the row data for the CSV.
    """
    filename = os.path.basename(file_path)
    try:
        result = parse_resume(file_path)
        if result:
            # Save JSON
            json_name = filename.rsplit('.', 1)[0] + ".json"
            with open(os.path.join(output_folder, json_name), 'w') as jf:
                json.dump(result, jf, indent=4)
            
            # Return data for the CSV logger
            return [filename, "SUCCESS", result['name'], result['email'], len(result['skills'])]
        else:
            return [filename, "FAILED", "", "", 0]
    except Exception as e:
        print(f"⚠️ Crash processing {filename}: {str(e)}")
        # Fail gracefully without crashing the whole batch
        return [filename, "ERROR", "", "", 0]

if __name__ == "__main__":
    # Define Paths
    base_dir = os.path.dirname(os.path.dirname(__file__)) # Go up to project root
    input_folder = os.path.join(base_dir, "data", "raw_resumes")
    output_folder = os.path.join(base_dir, "data", "processed")
    
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # CSV Log File for Reporting
    log_file = os.path.join(output_folder, "parsing_report.csv")
    
    print(f"🚀 Zecpath Parser V2.1 (Optimized Multi-threading) Starting...")
    print(f"📂 Reading from: {input_folder}")
    
    # Pre-filter files to avoid hidden system files like .DS_Store
    valid_files = []
    if os.path.exists(input_folder):
        for filename in os.listdir(input_folder):
            if filename.endswith((".pdf", ".docx")) and not filename.startswith('.'):
                valid_files.append(os.path.join(input_folder, filename))
    
    print(f"⚙️ Found {len(valid_files)} valid resumes. Commencing batch extraction...")

    with open(log_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        # Header Row
        writer.writerow(["Filename", "Status", "Name", "Email", "Skill Count"])

        # THE ENTERPRISE UPGRADE: Parallel Processing
        # max_workers=10 means processing 10 resumes simultaneously
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            # Schedule all files to be processed
            futures = {executor.submit(process_single_file, path, output_folder): path for path in valid_files}
            
            # As each file finishes processing, log its result to the CSV
            for future in concurrent.futures.as_completed(futures):
                row_data = future.result()
                writer.writerow(row_data)
                print(f"✅ Finished: {row_data[0]}")

    print(f"\n🏁 Done! Processed {len(valid_files)} resumes at maximum speed. Check 'data/processed' for results.")