def export_report_text(report):
    strengths_text = "\n".join(report['summary']['strengths']) if report['summary']['strengths'] else "None"
    risks_text = "\n".join(report['summary']['risks']) if report['summary']['risks'] else "None"
    missing_text = "\n".join(report['summary']['missing_data']) if report['summary']['missing_data'] else "None"
    skills_text = ", ".join(report['highlights']['confirmed_skills']) if report['highlights']['confirmed_skills'] else "None"

    text = f"""
Candidate ID: {report['candidate_id']}
Job ID: {report['job_id']}
Final Score: {report['final_score']}
Decision: {report['decision']}

--- Strengths ---
{strengths_text}

--- Risks ---
{risks_text}

--- Missing Data ---
{missing_text}

--- Highlights ---
Salary: {report['highlights']['salary_expectation']}
Availability: {report['highlights']['availability']}
Skills: {skills_text}
"""
    return text.strip()