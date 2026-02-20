import fitz  # PyMuPDF
import re
import spacy
import os
import json

# Load the AI Brain
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_details(text):
    data = {}
    
    # --- 1. PATTERN MATCHING (Regex) ---
    # Email
    email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
    data["email"] = email_match.group(0) if email_match else None

    # Phone
    phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\d{10})', text)
    data["phone"] = phone_match.group(0).strip() if phone_match else None

    # --- 2. ARTIFICIAL INTELLIGENCE (SpaCy) ---
    doc = nlp(text)
    
    # Extract Name (First PERSON entity)
    data["name"] = None
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            data["name"] = ent.text
            break

    # --- 3. SKILL EXTRACTION (Keyword Matching) ---
    # We define a list of skills we want to look for
    # (In a real app, this list would be huge or come from a database)
    skills_db = [
        "Python", "Java", "C++", "SQL", "JavaScript", "React", 
        "Angular", "Docker", "Kubernetes", "AWS", "Azure", 
        "Machine Learning", "Data Science", "Git", "Flask", "Django"
    ]
    
    found_skills = []
    # Convert text to lowercase to make matching easier
    text_lower = text.lower()
    
    for skill in skills_db:
        # Check if the skill (in lowercase) is in the text
        if skill.lower() in text_lower:
            found_skills.append(skill)
            
    data["skills"] = found_skills

    return data

if __name__ == "__main__":
    resume_path = os.path.join("data", "raw_resumes", "sample_resume.pdf")

    if os.path.exists(resume_path):
        print(f"Analyzing Resume with AI: {resume_path}...\n")
        raw_text = extract_text_from_pdf(resume_path)
        
        structured_data = extract_details(raw_text)

        print("--- FINAL JSON OUTPUT ---")
        print(json.dumps(structured_data, indent=4))
    else:
        print("Error: File not found.")