import re

class EducationParser:
    def __init__(self):
        # 1. Degree Level Normalization
        self.degree_levels = {
            "Doctorate": ["phd", "ph.d", "doctorate", "doctor of"],
            "Masters": ["master", "m.sc", "msc", "mba", "m.tech", "m.e", "m.s"],
            "Bachelors": ["bachelor", "b.sc", "bsc", "b.e", "b.e.", "b.tech", "b.a", "bba", "bs"]
        }
        
        # 2. Field of Study Relevance Mapping (For FinTech / Quant Roles)
        self.field_relevance = {
            "Highly Relevant": ["statistics", "mathematics", "finance", "economics", "quantitative", "computer science", "data science"],
            "Moderately Relevant": ["electronics", "communication", "engineering", "information technology", "business", "commerce"],
            "Low Relevance": ["arts", "history", "biology", "chemistry", "literature"]
        }

        # 3. NEW: Institution Keywords (Inspired by your friend's logic)
        self.institution_keywords = ["university", "college", "institute", "school", "academy", "polytechnic"]

    def parse_education(self, education_lines):
        """Extracts Degree, Field, Institution, and Year from text."""
        parsed_education = []
        text_block = " ".join(education_lines).lower()

        # UPGRADE 1: Smart Year Extraction (Looks for ranges like 2005 - 2009)
        graduation_year = "Unknown"
        range_match = re.search(r'\b(19[8-9]\d|20[0-3]\d)\s*[-–]\s*(19[8-9]\d|20[0-3]\d)\b', text_block)
        if range_match:
            graduation_year = range_match.group(2) # Grab the final completion year
        else:
            years = re.findall(r'\b(19[8-9]\d|20[0-3]\d)\b', text_block)
            if years:
                graduation_year = max(years)

        # UPGRADE 2: Institution Extraction
        detected_institution = "Unknown"
        for line in education_lines:
            # Split the line by commas or pipes to isolate the school name
            chunks = re.split(r'[|,]', line) 
            for chunk in chunks:
                if any(kw in chunk.lower() for kw in self.institution_keywords):
                    detected_institution = chunk.strip().title()
                    break
            if detected_institution != "Unknown":
                break

        # Normalize Degree Level
        detected_level = "Unknown"
        for level, keywords in self.degree_levels.items():
            if any(keyword in text_block for keyword in keywords):
                detected_level = level
                break

        # Normalize Field of Study & Calculate Relevance
        detected_field = "Unknown"
        relevance_category = "Low Relevance"
        relevance_score = 0.3 # Default low score

        # Check Highly Relevant fields
        for field in self.field_relevance["Highly Relevant"]:
            if field in text_block:
                detected_field = field.title()
                relevance_category = "Highly Relevant"
                relevance_score = 1.0
                break
        
        # If not high, check Moderately Relevant fields
        if relevance_category == "Low Relevance":
            for field in self.field_relevance["Moderately Relevant"]:
                if field in text_block:
                    detected_field = field.title()
                    relevance_category = "Moderately Relevant"
                    relevance_score = 0.8  
                    break

        parsed_education.append({
            "degree_level": detected_level,
            "field_of_study": detected_field,
            "institution": detected_institution, # NEW field added to output
            "graduation_year": graduation_year,
            "education_relevance_score": relevance_score,
            "raw_text": " | ".join(education_lines)
        })

        return parsed_education

    def parse_certifications(self, cert_lines):
        """Extracts and normalizes certifications."""
        parsed_certs = []
        high_value_certs = ["sql", "python", "aws", "cfa", "nptel", "power bi", "tableau", "machine learning"]

        for line in cert_lines:
            if not line.strip(): continue
            
            relevance = "General"
            if any(cert in line.lower() for cert in high_value_certs):
                relevance = "Highly Relevant to FinTech/Data"

            parsed_certs.append({
                "certification_name": line.strip(),
                "relevance": relevance
            })

        return parsed_certs