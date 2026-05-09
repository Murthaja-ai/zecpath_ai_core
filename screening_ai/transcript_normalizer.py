import re

def normalize_transcript(text: str) -> str:
    """
    Cleans raw audio transcripts by converting to lowercase, 
    stripping filler words, and resolving punctuation collisions.
    """
    if not text:
        return ""

    clean_text = text.lower()

    # 1. Define the junk words
    fillers = ["um", "uh", "like", "you know", "actually", "basically"]

    # 2. Destroy the filler words
    for f in fillers:
        clean_text = re.sub(rf"\b{f}\b", "", clean_text)

    # 3. The Ultimate Punctuation Sweep
    # Remove spaces before punctuation
    clean_text = re.sub(r'\s+([,?.!])', r'\1', clean_text)
    # Fix collisions: If a comma crashes into a period or question mark, delete the comma
    clean_text = re.sub(r',([?.!])', r'\1', clean_text)
    # Remove back-to-back commas
    clean_text = re.sub(r'[,]+(?=\s*[,])', '', clean_text)
    # Remove stray punctuation at the very beginning
    clean_text = re.sub(r'^[,?.!\s]+', '', clean_text)

    # 4. Clean up weird double spaces
    clean_text = re.sub(r"\s+", " ", clean_text)

    return clean_text.strip()


# --- Quick Test ---
if __name__ == "__main__":
    messy_audio = "Um, yeah, so like, I basically have 3 years of experience, you know?"
    print(f"🎙️ Raw Audio: '{messy_audio}'")
    
    clean_audio = normalize_transcript(messy_audio)
    print(f"✨ Cleaned Text: '{clean_audio}'")