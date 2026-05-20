import re

def clean_noise(text: str) -> str:
    """Sanitizes raw STT text by removing noise markers and stutters."""
    if not text:
        return ""
        
    # 1. Remove background noise markers like [cough], [wind], [unintelligible]
    text = re.sub(r"\[.*?\]", "", text)
    
    # 2. Remove severe repeated characters (e.g., 'hhhello' -> 'hello')
    text = re.sub(r"(.)\1{2,}", r"\1", text)
    
    # 3. NEW: Collapse multiple spaces into a single space
    text = re.sub(r"\s+", " ", text)
    
    return text.strip()