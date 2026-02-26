import re

class ResumeSegmenter:
    def __init__(self):
        # The Master Dictionary of Section Headers
        self.HEADER_PATTERNS = {
            "EXPERIENCE": [
                r"experience", r"work experience", r"work history", r"employment", 
                r"employment history", r"professional experience", r"career history", 
                r"professional background", r"job history"
            ],
            "EDUCATION": [
                r"education", r"academic background", r"academic history", 
                r"qualifications", r"educational qualifications", r"college", 
                r"university", r"schooling"
            ],
            "SKILLS": [
                r"skills", r"technical skills", r"core competencies", r"technologies", 
                r"tech stack", r"programming languages", r"expertise", r"proficiencies"
            ],
            "PROJECTS": [
                r"projects", r"personal projects", r"academic projects", 
                r"key projects", r"capstone projects"
            ],
            "CERTIFICATIONS": [
                r"certifications", r"certificates", r"courses", r"licenses", 
                r"trainings", r"achievements", r"awards"
            ],
            "CONTACT": [
                r"contact", r"contact info", r"contact details", r"reach me", 
                r"personal info", r"about me"
            ]
        }

    def clean_header(self, text):
        """Removes special characters to see if a line is a header."""
        return re.sub(r"[^a-zA-Z\s]", "", text).strip().lower()

    def detect_header(self, line):
        """Checks if a single line of text looks like a known header."""
        clean_line = self.clean_header(line)
        
        # Rule 1: Headers are usually short (under 5 words)
        if len(clean_line.split()) > 5: 
            return None

        # Rule 2: Check our dictionary
        for section, patterns in self.HEADER_PATTERNS.items():
            for pattern in patterns:
                # We use fullmatch because headers usually take up the whole line
                if re.fullmatch(pattern, clean_line):
                    return section
        
        return None

    def segment(self, text):
        """The Main Function: Slices the resume text into sections."""
        
        # 1. Initialize our "Buckets"
        sections = {
            "CONTACT": [],
            "EXPERIENCE": [],
            "EDUCATION": [],
            "SKILLS": [],
            "PROJECTS": [],
            "CERTIFICATIONS": [],
            "SUMMARY": []  # Default bucket for text at the top
        }
        
        current_section = "SUMMARY"  # Start by assuming text is a summary
        
        # 2. Split text into lines and walk through them
        lines = text.split('\n')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue  # Skip empty lines
            
            # 3. Check: Is this line a Header?
            detected_header = self.detect_header(line)
            
            if detected_header:
                # YES -> Switch buckets!
                current_section = detected_header
            else:
                # NO -> Put line into current bucket
                sections[current_section].append(line)
        
        return sections

# --- Test Block ---
if __name__ == "__main__":
    # A fake resume text to test our logic
    sample_resume = """
    Murthaja
    Software Developer | Kerala, India
    
    *** Professional Experience ***
    Software Engineer at TechCorp
    - Built Angular apps
    - Used Python for backend
    
    EDUCATION
    B.Tech in Computer Science
    University of Calicut
    
    Technical Skills
    Python, Angular, SQL, MongoDB
    """

    segmenter = ResumeSegmenter()
    segmented_data = segmenter.segment(sample_resume)
    
    import json
    print(json.dumps(segmented_data, indent=4))