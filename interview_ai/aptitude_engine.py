# interview_ai/aptitude_engine.py

# Advanced Heuristic Dictionaries
STRUCTURE_MARKERS = ["first", "then", "next", "finally", "step", "initially"]
CAUSE_EFFECT_MARKERS = ["because", "therefore", "due to", "as a result", "consequently"]
TRADEOFF_MARKERS = ["risk", "alternative", "however", "fallback", "instead", "weigh", "pros and cons"]

SCENARIO_PATTERNS = {
    "team_conflict": ["communicate", "listen", "understand", "resolve", "align", "discuss"],
    "deadline_pressure": ["prioritize", "delegate", "communicate", "mvp", "critical"],
    "learning": ["documentation", "research", "practice", "sandbox", "apply"]
}

def score_logic_structure(text: str) -> float:
    """Evaluates if the candidate thinks sequentially and uses cause-and-effect."""
    text = text.lower()
    seq_count = sum(text.count(word) for word in STRUCTURE_MARKERS)
    cause_count = sum(text.count(word) for word in CAUSE_EFFECT_MARKERS)
    
    total_logic_markers = seq_count + (cause_count * 1.5) # Cause-and-effect is weighted higher
    
    if total_logic_markers >= 3: return 1.0
    if total_logic_markers >= 1: return 0.7
    return 0.4

def score_risk_awareness(text: str) -> float:
    """Evaluates if the candidate considers trade-offs or fallback plans."""
    text = text.lower()
    tradeoff_count = sum(text.count(word) for word in TRADEOFF_MARKERS)
    
    if tradeoff_count >= 2: return 1.0
    if tradeoff_count == 1: return 0.8
    return 0.5 # Default baseline for an answer with no risk awareness

def evaluate_scenario_alignment(text: str, scenario_type: str) -> float:
    """Checks how well the candidate hits the specific milestones for a given crisis."""
    text = text.lower()
    patterns = SCENARIO_PATTERNS.get(scenario_type, [])
    
    if not patterns:
        return 0.5 # Neutral if unknown scenario
        
    match_count = sum(1 for word in patterns if word in text)
    match_ratio = match_count / len(patterns)
    
    if match_ratio >= 0.6: return 1.0 # Hit the majority of key points
    if match_ratio >= 0.3: return 0.7
    return 0.4

def calculate_aptitude_profile(text: str, scenario_type: str = "deadline_pressure") -> dict:
    """The Master Pipeline for Cognitive Evaluation."""
    if not text.strip():
        return {"aptitude_score": 0.0}

    structure = score_logic_structure(text)
    risk = score_risk_awareness(text)
    scenario = evaluate_scenario_alignment(text, scenario_type)
    
    # Formula: 40% Structure + 20% Risk/Tradeoffs + 40% Scenario Alignment
    final_score = (structure * 0.40) + (risk * 0.20) + (scenario * 0.40)
    
    return {
        "aptitude_score": round(final_score * 100, 2),
        "scenario_type": scenario_type,
        "breakdown": {
            "structured_thinking": round(structure * 100, 2),
            "risk_awareness": round(risk * 100, 2),
            "scenario_alignment": round(scenario * 100, 2)
        }
    }