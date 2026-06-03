# interview_ai/summary_generator.py

def extract_strengths(hr_report, aptitude_report, comm_score):
    """Translates high scores into professional HR strength statements."""
    strengths = []
    if hr_report.get("final_hr_score", 0) >= 80:
        strengths.append("High technical relevance and role alignment")
    if comm_score >= 80:
        strengths.append("Exceptional communication fluency and clarity")
    if aptitude_report.get("aptitude_score", 0) >= 80:
        strengths.append("Advanced structured thinking and problem-solving logic")
    return strengths if strengths else ["No major outstanding strengths identified"]

def extract_weaknesses(hr_report, aptitude_report, comm_score):
    """Translates low scores into professional HR weakness statements."""
    weaknesses = []
    if hr_report.get("final_hr_score", 100) < 60:
        weaknesses.append("Struggled with core technical requirements")
    if comm_score < 60:
        weaknesses.append("Communication lacked structure or relied on filler words")
    if aptitude_report.get("breakdown", {}).get("structured_thinking", 100) < 50:
        weaknesses.append("Answers to crisis scenarios lacked sequential logic")
    return weaknesses if weaknesses else ["No critical weaknesses identified"]

def extract_risk_flags(behavioral_profile, aptitude_report):
    """Hunts for critical red flags (backpedaling, panic, recklessness)."""
    risks = []
    if behavioral_profile.get("contradiction_detected"):
        risks.append("CRITICAL: Candidate backpedaled or contradicted their own technical claims.")
    if behavioral_profile.get("behavioral_score", 100) < 50:
        risks.append("WARNING: Displayed high hesitation or stress indicators under pressure.")
    if aptitude_report.get("breakdown", {}).get("risk_awareness", 100) < 50:
        risks.append("WARNING: Showed poor risk evaluation; failed to consider trade-offs.")
    return risks

def generate_professional_narrative(strengths, weaknesses, risks, decision):
    """Compiles the parsed data into a fluid, human-readable paragraph."""
    narrative = "Executive Summary:\n"
    
    # Strengths sentence
    if "No major" not in strengths[0]:
        narrative += f"The candidate demonstrated strong capabilities, particularly in {strengths[0].lower()}"
        if len(strengths) > 1:
            narrative += f" and {strengths[1].lower()}."
        else:
            narrative += "."
    else:
        narrative += "The candidate met baseline requirements but did not display exceptional standout strengths."

    # Weaknesses & Risks sentence
    if risks:
        narrative += f" However, severe risk factors were identified, notably: {risks[0].lower()}"
    elif "No critical" not in weaknesses[0]:
        narrative += f" Areas for improvement include {weaknesses[0].lower()}."

    narrative += f"\nFinal System Recommendation: {decision.upper()}"
    return narrative

def generate_interview_summary(candidate_id, hr_report, aptitude_report, comm_score, behavioral_profile):
    """The Master Pipeline for the Day 39 Summary Generator."""
    
    # Extract insights using our upgraded heuristics
    strengths = extract_strengths(hr_report, aptitude_report, comm_score)
    weaknesses = extract_weaknesses(hr_report, aptitude_report, comm_score)
    risks = extract_risk_flags(behavioral_profile, aptitude_report)
    
    # We do NOT recalculate the score. We average the two master engines (HR and Aptitude).
    composite_score = (hr_report.get("final_hr_score", 0) + aptitude_report.get("aptitude_score", 0)) / 2
    
    decision = "STRONG HIRE" if composite_score >= 75 else "CONSIDER" if composite_score >= 55 else "REJECT"

    narrative = generate_professional_narrative(strengths, weaknesses, risks, decision)

    return {
        "candidate_id": candidate_id,
        "composite_score": round(composite_score, 2),
        "decision": decision,
        "structured_insights": {
            "strengths": strengths,
            "weaknesses": weaknesses,
            "risk_flags": risks
        },
        "executive_narrative": narrative
    }