# Zecpath - AI-Powered Autonomous Hiring Platform

## 📌 Executive Overview
Zecpath is an end-to-end, AI-first hiring platform designed to fully automate the recruitment lifecycle—from initial resume screening to final offer letter generation. As outlined in the Zecpath 100-Phase Product Requirements Document (PRD), this system eliminates manual HR workloads through AI-driven Applicant Tracking, natural-sounding multilingual Voice AI interviews, behavioral analysis, adaptive technical evaluations, and automated decision-making.

This repository (`zecpath_ai_core`) contains the foundational backend architecture, structured as a Monorepo containing four distinct enterprise microservices:

1. **The ATS Document Engine (Phases 1-2):** Ingests raw resumes, extracts technical skills via custom Knowledge Graphs, calculates experience relevance, and ranks candidates against job descriptions.
2. **The Voice Screening AI (Phases 3-10):** An automated HR caller that reads the ATS shortlist, conducts 5-minute dynamic voice interviews, grades answers mathematically, handles edge-case chaos (noise/language mixing), and serves the results via a secure API.
3. **The Advanced HR Interviewer (Phases 11-25):** A deep, 30-minute psychological evaluation engine. It features dynamic role-based question playlists, a 4-phase state machine (Intro, Core, Role, Closing), and real-time empathy heuristics to trigger follow-up questions.
4. **The Technical Interview System (Phase 7 / Day 46+):** An adaptive technical evaluation engine with a dynamic hysteresis difficulty progression, multi-domain skill hierarchy (MERN, Java, Data Science, DevOps), and automated system-design probing for senior candidates.
5. **The Behavioral AI Engine (Phase 8 / Day 48+):** A context-aware, non-invasive visual telemetry analyzer. It monitors eye focus, head stability, and engagement, dynamically adjusting its strictness based on the live interview phase to detect true distraction without penalizing natural cognitive reflection.
6. **The Integrity & Security Shield (Phase 9 / Day 49+):** A non-invasive digital proctoring engine. It monitors tab-switching, browser focus loss, and external voice anomalies. It utilizes compounding heuristics and integrates directly with the behavioral context to catch coordinated cheating without penalizing honest candidates.
7. **The Machine Test Engine (Phase 10 / Day 50+):** A practical execution sandbox evaluator. It grades live coding and system design tasks using continuous mathematical decay for runtime/efficiency, structural code quality checks, and features a strict data-interlock with the Phase 9 Integrity Shield to nullify fraudulent submissions.
8. **Cross-Round Aggregation Engine (Phase 11 / Day 51+):** The unified scoring brain. It aggregates data from the ATS, Voice AI, HR modules, and Technical sandboxes. It features dynamic residual re-weighting for missing data, cohort-based normalization, and dynamically generates Explainable AI (XAI) summaries for recruiters.
9. **Final Recommendation AI (Phase 12 / Day 52+):** The ultimate decision-making CEO engine. It applies hybrid rule/score logic, utilizing Hard Gate Overrides to reject high-scoring but high-risk candidates (e.g., cheaters), calculates a Multi-Factor Confidence Index, and generates defensible Explainable AI hiring narratives.
10. **Hiring Intelligence Report Generator (Phase 13 / Day 53+):** The presentation layer. It compiles the vast telemetry from all preceding evaluation phases (ATS, Screening, Tech, Behavioral, and Final Decision) into a single, structured, export-ready Markdown dossier utilizing BLUF (Bottom Line Up Front) architecture.
11. **Optimization & Refinement (Phase 14 / Day 54+):** The performance tuning layer. Upgrades the system from a functional prototype to an enterprise-grade pipeline by implementing statistical standard-deviation scoring, strict Hard-Gate edge case resolution, and asynchronous concurrent batch processing.
12. **Security & AI Governance (Phase 15 / Day 55):** The enterprise compliance vault. Enforces strict Role-Based Access Control (RBAC), mandates candidate consent gates, utilizes AES-256 persistent encryption for sensitive PII, and generates immutable JSON-Lines audit trails for legal defensibility.
13. **Full System Simulation (Phase 16 / Day 56):** The E2E integration orchestrator. Connects the Scoring, Optimization, and Security cores to process candidate personas. Validates that Hard Gates, Standard Deviation penalties, and Compliance barriers function cohesively as a unified enterprise architecture.
14. **System Hardening & Stabilization (Phase 17 / Day 57):** The production-readiness layer. Engineered middleware shock-absorbers (Data Sanitization, NLP Guards, and API Formatters) to intercept corrupted data, preventing catastrophic runtime exceptions and guaranteeing predictable JSON payloads for frontend integration.
15. **V2.0 Advanced Feature Architecture (Phase 18 / Day 58):** Transitioned from backend development to product strategy. Designed a legally compliant (EU AI Act) behavioral analytics roadmap, mapped an AWS serverless scaling strategy, and prototyped an LLM-driven AI Coaching system to provide empathetic, variance-based feedback to rejected candidates.
16. **API Architecture & Integration Planning (Phase 19 / Day 59):** Designed and deployed the master API contracts bridging the AI core with external systems. Implemented non-blocking asynchronous task pooling handlers for resource-heavy operations (e.g., PDF processing) to preserve frontend UI stability, engineered strict JWT/Bearer request verification middlewares, and enforced the standardized system output envelope across all unified network endpoints.



## 🗂️ System Documentation Hub
Because of the massive scale of this enterprise architecture, technical documentation is split by microservice. Click the links below to view the detailed architecture, file structures, and execution commands for each system:

* ➡️ **[Phase 1: ATS & Document Intelligence (Days 1 - 21)](./parsers/README.md)**
* ➡️ **[Phase 2: Voice Screening AI & API (Days 22 - 32)](./screening_ai/README.md)**
* ➡️ **[Phase 3: Advanced HR Interview Architecture (Day 33 - 45)](./interview_ai/README.md)**
* ➡️ **[Phase 7: Technical Interview AI System (Day 46+)](./technical_ai/README.md)**
* ➡️ **[Phase 8: Behavioral AI & Engagement Analysis (Day 48+)](./behavior_ai/README.md)**
* ➡️ **[Phase 9: Integrity & Malpractice Detection (Day 49+)](./integrity_ai/README.md)**
* ➡️ **[Phase 10: Machine Test Practical Evaluation (Day 50+)](./machine_test/README.md)**
* ➡️ **[Phase 11: Cross-Round Aggregation Engine (Day 51+)](./aggregation_core/README.md)**
* ➡️ **[Phase 12: Final Recommendation AI (Day 52+)](./recommendation_core/README.md)**
* ➡️ **[Phase 13: Hiring Intelligence Report Generator (Day 53+)](./reporting_core/README.md)**
* ➡️ **[Phase 14: System Optimization & Refinement (Day 54+)](./optimization_core/README.md)**
* ➡️ **[Phase 15: Security & AI Governance (Day 55)](./security_core/README.md)**
* ➡️ **[Phase 16: Full System Simulation (Day 56)](./simulation_core/README.md)**
* ➡️ **[Phase 17: Debugging & System Stabilization (Day 57)](./stabilization_core/README.md)**
* ➡️ **[Phase 18: V2.0 Advanced Feature Architecture (Day 58)](./advanced_features_v2/ROADMAP_V2.md)**
* ➡️ **[Phase 19: API Architecture & Integration Planning (Day 59)](./api_integration/API_CONTRACT.md)**

## 🚀 Global Setup & Installation

**1. Clone the repository**
git clone https://github.com/Murthaja-ai/zecpath_ai_core.git
cd zecpath_ai_core

**2. Create and activate a Virtual Environment**
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

**3. Install Dependencies**
pip install -r requirements.txt
pip install sentence-transformers torch flask pytest