# interview_ai/communication_engine.py
import re

FILLER_WORDS = ["um", "uh", "like", "you know", "actually", "basically"]

def score_fluency(text: str) -> float:
    """Measures sentence continuity by counting valid sentences."""
    sentences = re.split(r'[.!?]', text)
    valid_sentences = [s for s in sentences if len(s.split()) > 3]
    if len(valid_sentences) >= 2:
        return 1.0
    elif len(valid_sentences) == 1:
        return 0.6
    return 0.3

def score_grammar(text: str) -> float:
    """Basic heuristic checking for capitalization and punctuation."""
    if text and text[0].isupper() and text.strip().endswith(('.', '?', '!')):
        return 1.0
    elif len(text.split()) > 5:
        return 0.7
    return 0.4

def score_vocabulary(text: str) -> float:
    """Measures lexical diversity (ratio of unique words)."""
    words = text.lower().split()
    if not words: return 0.0
    unique_words = set(words)
    if len(unique_words) / (len(words) + 1) > 0.6:
        return 1.0
    elif len(unique_words) > 5:
        return 0.7
    return 0.4

def score_clarity(text: str) -> float:
    """Measures answer depth via word count."""
    length = len(text.split())
    if length > 12:
        return 1.0
    elif length > 6:
        return 0.7
    return 0.4

def filler_penalty(text: str) -> float:
    """Calculates a deduction based on crutch words."""
    text = text.lower()
    count = sum(text.count(word) for word in FILLER_WORDS)
    penalty = min(count * 0.1, 0.5) # Max penalty is 0.5
    return penalty

def score_structure(text: str) -> float:
    """Checks for logical transition words."""
    if "because" in text.lower() or "for example" in text.lower():
        return 1.0
    elif len(text.split()) > 6:
        return 0.7
    return 0.4

def calculate_communication_score(text: str) -> dict:
    """Master formula combining all metrics into a 0-100 score."""
    if not text.strip():
        return {"communication_score": 0.0, "breakdown": {}}
        
    fluency = score_fluency(text)
    grammar = score_grammar(text)
    vocab = score_vocabulary(text)
    clarity = score_clarity(text)
    structure = score_structure(text)
    penalty = filler_penalty(text)
    
    # 20% weight for each of the 5 categories
    raw_score = (fluency * 0.2 + grammar * 0.2 + vocab * 0.2 + clarity * 0.2 + structure * 0.2)
    final_score = max(raw_score - penalty, 0)
    
    return {
        "communication_score": round(final_score * 100, 2),
        "breakdown": {
            "fluency": round(fluency, 2),
            "grammar": round(grammar, 2),
            "vocabulary": round(vocab, 2),
            "clarity": round(clarity, 2),
            "structure": round(structure, 2),
            "penalty": round(penalty, 2)
        }
    }