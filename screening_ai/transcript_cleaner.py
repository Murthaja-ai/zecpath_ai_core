from screening_ai.transcript_normalizer import normalize_transcript

def process_audio_answers(raw_text_list: list) -> list:
    """
    Takes a list of raw STT text strings, cleans them, 
    and assigns a sequential Question ID.
    """
    results = []
    for idx, raw_text in enumerate(raw_text_list):
        if not raw_text or len(raw_text.strip()) < 2:
            status = "silence_detected"
            clean_text = ""
        else:
            status = "processed"
            clean_text = normalize_transcript(raw_text)

        results.append({
            "question_id": f"Q{idx+1}",
            "clean_text": clean_text,
            "status": status
        })
    return results

if __name__ == "__main__":
    inputs = [
        "um i have 3 years experience in python",
        "uh currently working as backend developer",
        ""
    ]
    print(process_audio_answers(inputs))