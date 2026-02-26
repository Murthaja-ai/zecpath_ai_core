import fitz  # PyMuPDF
import re
import spacy
import os
import json

class ResumeParser:
    def __init__(self):
        # Load the AI Brain once when the class is created
        print("🧠 Loading SpaCy Model...")
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("⚠️ Warning: SpaCy model 'en_core_web_sm' not found. extracting keywords only.")
            self.nlp = None

    def extract_text(self, pdf_path):
        """Reads a PDF file and returns the raw text string."""
        try:
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text()
            return text
        except Exception as e:
            return f"Error reading PDF: {str(e)}"

    def extract_details(self, text):
        """
        Runs Regex and NLP to find Email, Phone, Name, and Skills.
        """
        data = {}
        
        # --- 1. PATTERN MATCHING (Regex) ---
        # Email
        email_match = re.search(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)
        data["email"] = email_match.group(0) if email_match else None

        # Phone
        phone_match = re.search(r'(\+?\d{1,3}[-.\s]?)?(\d{10})', text)
        data["phone"] = phone_match.group(0).strip() if phone_match else None

        # --- 2. ARTIFICIAL INTELLIGENCE (SpaCy) ---
        data["name"] = None
        if self.nlp:
            doc = self.nlp(text)
            # Extract Name (First PERSON entity)
            for ent in doc.ents:
                if ent.label_ == "PERSON":
                    data["name"] = ent.text
                    break

        # --- 3. SKILL EXTRACTION (Keyword Matching) ---
        skills_db = [
            "Python", "Java", "C++", "SQL", "JavaScript", "React", 
            "Angular", "Docker", "Kubernetes", "AWS", "Azure", 
            "Machine Learning", "Data Science", "Git", "Flask", "Django"
        ]
        
        found_skills = []
        text_lower = text.lower()
        
        for skill in skills_db:
            if skill.lower() in text_lower:
                found_skills.append(skill)
                
        data["skills"] = list(set(found_skills)) # Remove duplicates

        return data

# --- Test Block ---
if __name__ == "__main__":
    # This block only runs if you run this file directly
    parser = ResumeParser()
    
    # Update this path if you want to test a specific file
    test_pdf_path = os.path.join("data", "raw_resumes", "sample_resume.pdf")

    if os.path.exists(test_pdf_path):
        print(f"📄 Analyzing: {test_pdf_path}...")
        raw_text = parser.extract_text(test_pdf_path)
        structured_data = parser.extract_details(raw_text)
        print(json.dumps(structured_data, indent=4))
    else:
        print("ℹ️ To test, place a PDF at data/raw_resumes/sample_resume.pdf")