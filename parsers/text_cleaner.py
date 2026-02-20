import re

def clean_text(text):
    """
    Standardizes text while preserving line structure.
    """
    if not text:
        return ""

    # 1. Normalize bullet points
    text = re.sub(r"[•●▪■➤]", "-", text)
    
    # 2. Remove weird non-ascii characters
    text = text.encode("ascii", "ignore").decode()
    
    # 3. Fix multiple spaces but KEEP newlines (Critical Fix)
    # The old code 're.sub(r'\s+', ' ', text)' destroyed newlines.
    # This new code only fixes horizontal spaces (tabs/spaces).
    text = re.sub(r'[ \t]+', ' ', text)
    
    # 4. Fix excessive newlines (max 2)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    return text.strip()