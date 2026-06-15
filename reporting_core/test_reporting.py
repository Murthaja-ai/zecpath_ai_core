# reporting_core/test_reporting.py
import json
from report_compiler import HiringReportCompiler
from report_formatter import ExecutiveReportFormatter

def run_e2e_reporting_pipeline():
    print("📋 Initializing Day 53 Enterprise Report Generator Subsystem...\n")

    # Mock Input Data mirroring the output from Phase 11 & Phase 12
    mock_phase_11 = {
        "normalized_scores": {
            "ats_resume_match": 85.0,
            "screening_round": 80.0,
            "hr_behavioral": 88.0,
            "technical_architecture": 90.0,
            "practical_machine_test": 85.0
        }
    }

    mock_phase_12 = {
        "candidate_id": "C12001",
        "final_recommendation": "Selected",
        "ai_confidence_index": 100.0,
        "scoring_telemetry": {
            "raw_unified_score": 86.0,
            "risk_adjusted_score": 86.0,
        },
        "risk_profile": {
            "behavioral_status": "Low Risk",
            "integrity_status": "Low Risk"
        },
        "automated_explanation": {
            "rationale_narrative": "Candidate achieved a strong adjusted score of 86.0% with acceptable risk margins. Recommended for immediate offer.",
            "identified_strengths": ["Strong technical/aggregate foundation.", "Excellent behavioral alignment."],
            "weaknesses": []
        }
    }

    # 1. Execute Compilation
    compiled_profile = HiringReportCompiler.compile_master_profile(mock_phase_11, mock_phase_12)
    
    # 2. Execute Formatting
    markdown_report = ExecutiveReportFormatter.to_markdown_dossier(compiled_profile)
    json_export = ExecutiveReportFormatter.to_json_export(compiled_profile)

    print("✔ [Pipeline Success] Master Profile Object Compiled.")
    print("✔ [Pipeline Success] Export-Ready Layouts Rendered.\n")
    print("="*40 + " DISPLAYING RECRUITER VIEW " + "="*40 + "\n")
    print(markdown_report)
    print("\n" + "="*107)

if __name__ == "__main__":
    run_e2e_reporting_pipeline()