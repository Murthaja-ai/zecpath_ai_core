import re

def normalize_transcript(text: str) -> str:
    """
    Cleans raw audio transcripts by stripping filler words, 
    fixing stutters, and formatting final punctuation.
    """
    if not text:
        return ""

    clean_text = text.lower()

    # --- DAY 24 UPDATE 1: Handle Interruptions/Stutters (e.g., "ummm" -> "um") ---
    clean_text = re.sub(r"(.)\1{2,}", r"\1", clean_text)

    # Define the junk words
    fillers = ["um", "uh", "like", "you know", "actually", "basically", "hmm"]

    # Destroy the filler words
    for f in fillers:
        clean_text = re.sub(rf"\b{f}\b", "", clean_text)

    # Punctuation Sweep (from Day 23)
    clean_text = re.sub(r'\s+([,?.!])', r'\1', clean_text)
    clean_text = re.sub(r',([?.!])', r'\1', clean_text)
    clean_text = re.sub(r'[,]+(?=\s*[,])', '', clean_text)
    clean_text = re.sub(r'^[,?.!\s]+', '', clean_text)
    clean_text = re.sub(r"\s+", " ", clean_text).strip()

    # --- DAY 24 UPDATE 2: Final Formatting (Capitalize and add period) ---
    if clean_text:
        clean_text = clean_text[0].upper() + clean_text[1:]
        if not clean_text.endswith((".", "!", "?")):
            clean_text += "."

    return clean_text

# --- Quick Test ---
if __name__ == "__main__":
    messy_audio = "ummm, yeah, so like, I basically have 3 years of experience, you know?"
    clean_audio = normalize_transcript(messy_audio)
    print(f"✨ Cleaned Text: '{clean_audio}'")