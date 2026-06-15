# reporting_core/report_formatter.py

class ExecutiveReportFormatter:
    @staticmethod
    def to_json_export(master_profile: dict) -> dict:
        """Wraps the master profile inside an export-compliant schema block."""
        return {
            "export_metadata": {
                "format": "JSON_INTELLIGENCE_REPORT",
                "status": "APPROVED"
            },
            "profile": master_profile
        }

    @staticmethod
    def to_markdown_dossier(master_profile: dict) -> str:
        """Converts the compiled candidate telemetry into a clean executive report."""
        meta = master_profile["metadata"]
        summary = master_profile["executive_summary"]
        scores = master_profile["score_matrix"]["stages"]
        risks = master_profile["compliance_and_risks"]
        highlights = master_profile["evaluation_highlights"]

        # Build clean visual boundaries using Markdown
        markdown = []
        markdown.append(f"# ZECPATH TALENT ACQUISITION: EXECUTIVE EVALUATION REPORT")
        markdown.append(f"**Candidate Tracking ID:** {meta['candidate_id']} | **System Blueprint:** {meta['engine_version']}")
        markdown.append(f"---")
        
        markdown.append(f"## ⚡ 1. EXECUTIVE ACTION SUMMARY")
        markdown.append(f"* **FINAL RECOMMENDATION:** **{summary['final_action'].upper()}**")
        markdown.append(f"* **AI DECISION CONFIDENCE:** `{summary['ai_confidence_rating']}`")
        markdown.append(f"* **RAW AGGREGATE PERFORMANCE:** {summary['raw_aggregate_score']}%")
        markdown.append(f"* **RISK-ADJUSTED SCORE:** {summary['risk_adjusted_score']}%")
        markdown.append(f"\n> **AI Decision Rationale:** {summary['hiring_rationale']}")
        markdown.append(f"---")

        markdown.append(f"## 📊 2. MULTI-STAGE SCORE BREAKDOWN")
        for stage, score in scores.items():
            markdown.append(f"* **{stage.replace('_', ' ').title()}:** `{score}%`")
        markdown.append(f"---")

        markdown.append(f"## 🛡️ 3. COMPLIANCE & RISK METRICS")
        markdown.append(f"* **Behavioral Analysis Risk Factor:** `{risks['behavioral_risk_level']}`")
        markdown.append(f"* **Integrity Verification Risk Factor:** `{risks['integrity_risk_level']}`")
        markdown.append(f"---")

        markdown.append(f"## 💡 4. EVALUATION HIGHLIGHTS")
        markdown.append(f"### 👍 Identified Assets & Strengths:")
        if highlights["strengths"]:
            for strg in highlights["strengths"]:
                markdown.append(f"  - {strg}")
        else:
            markdown.append(f"  - No exceptional strengths logged.")

        markdown.append(f"\n### ⚠️ Identified Vulnerabilities & Gaps:")
        if highlights["weaknesses"]:
            for weak in highlights["weaknesses"]:
                markdown.append(f"  - {weak}")
        else:
            markdown.append(f"  - No critical performance gaps logged.")

        return "\n".join(markdown)