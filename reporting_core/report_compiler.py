# reporting_core/report_compiler.py

class HiringReportCompiler:
    @staticmethod
    def compile_master_profile(phase_11_scores: dict, phase_12_decision: dict) -> dict:
        """
        Ingests the complete outputs from the Aggregation Engine (Phase 11)
        and Decision Brain (Phase 12) to build a unified profile dossier.
        """
        # Extract metadata safely
        candidate_id = phase_12_decision.get("candidate_id", "UNKNOWN")
        recommendation = phase_12_decision.get("final_recommendation", "Rejected")
        confidence = phase_12_decision.get("ai_confidence_index", 0.0)
        telemetry = phase_12_decision.get("scoring_telemetry", {})
        risks = phase_12_decision.get("risk_profile", {})
        explanation = phase_12_decision.get("automated_explanation", {})

        # Compile into a single structured corporate document object
        master_profile = {
            "metadata": {
                "candidate_id": candidate_id,
                "document_type": "Hiring Intelligence Report",
                "engine_version": "v12.2"
            },
            "executive_summary": {
                "final_action": recommendation,
                "ai_confidence_rating": f"{confidence}%",
                "raw_aggregate_score": telemetry.get("raw_unified_score", 0.0),
                "risk_adjusted_score": telemetry.get("risk_adjusted_score", 0.0),
                "hiring_rationale": explanation.get("rationale_narrative", "No narrative provided.")
            },
            "score_matrix": {
                "stages": phase_11_scores.get("normalized_scores", phase_11_scores)
            },
            "compliance_and_risks": {
                "behavioral_risk_level": risks.get("behavioral_status", "Unknown"),
                "integrity_risk_level": risks.get("integrity_status", "Unknown")
            },
            "evaluation_highlights": {
                "strengths": explanation.get("identified_strengths", []),
                "weaknesses": explanation.get("identified_weaknesses", [])
            }
        }
        return master_profile