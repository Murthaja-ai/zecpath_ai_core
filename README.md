# Zecpath - AI-Powered Autonomous Hiring Platform (v1.0 Core)

![Status: Release Ready](https://img.shields.io/badge/Status-Release%20Ready-success)
![Version](https://img.shields.io/badge/Version-1.0-blue)
![Architecture](https://img.shields.io/badge/Architecture-Microservices-purple)
![PRD Alignment](https://img.shields.io/badge/PRD_Alignment-Phases_1--75-orange)

## 📌 Executive Overview
Zecpath is an end-to-end, AI-first hiring platform designed to fully automate the recruitment lifecycle. As outlined in the **Zecpath 100-Phase Product Requirements Document (PRD)**, this system eliminates manual HR workloads through AI-driven Applicant Tracking, natural-sounding multilingual Voice AI interviews, behavioral analysis, adaptive technical evaluations, and automated decision-making.

This repository (`zecpath_ai_core`) contains the foundational **v1.0 backend architecture**, successfully implementing **PRD Phases 1 through 75** (from ATS Ingestion to Final Hiring Recommendation). It is structured as a Monorepo containing the following enterprise microservices:

1. **The ATS Document Engine (PRD Phase 1-2):** Ingests raw resumes, extracts technical skills via custom Knowledge Graphs, calculates experience relevance, and ranks candidates against job descriptions.
2. **The Voice Screening AI (PRD Phase 3-10):** An automated HR caller that reads the ATS shortlist, conducts dynamic voice interviews, grades answers mathematically, and handles edge-case chaos.
3. **The Advanced HR Interviewer (PRD Phase 11-25):** A 30-minute psychological video evaluation engine. It features dynamic role-based question playlists and real-time empathy heuristics.
4. **The Technical Interview System (PRD Phase 26-50):** An adaptive technical evaluation engine with dynamic difficulty progression, multi-domain skill hierarchy, and automated system-design probing.
5. **The Machine Test Engine (PRD Phase 51-75):** A practical execution sandbox evaluator. Grades live coding tasks using continuous mathematical decay for runtime/efficiency.
6. **The Behavioral AI Engine:** A context-aware, non-invasive visual telemetry analyzer. Monitors eye focus and engagement during video interviews, dynamically adjusting strictness based on the live phase.
7. **The Integrity & Security Shield:** A non-invasive digital proctoring engine. Monitors tab-switching and browser focus loss to catch coordinated cheating without penalizing honest candidates.
8. **Cross-Round Aggregation Engine:** The unified scoring brain. Aggregates data from ATS, Voice AI, HR modules, and Technical sandboxes via a Statistical Variance penalty model.
9. **Final Recommendation AI:** The ultimate decision-making CEO engine. Applies hybrid rule/score logic, utilizing Hard Gate Overrides to reject high-scoring but high-risk candidates.
10. **Hiring Intelligence Report Generator:** Compiles vast telemetry from all preceding evaluation phases into a single, structured, export-ready Markdown dossier.

---

## 🚀 v2.0 Roadmap & Future Scope (PRD Phases 76 - 100)
While v1.0 covers the core evaluation pipeline, the architecture is primed for the final PRD integration phases:
* **AI Salary Negotiation Engine (Phases 76-90):** An autonomous negotiation module that balances company budget constraints, candidate skills, and market benchmarks to finalize offers dynamically.
* **Offer Letter Automation (Phases 91-100):** Automated generation of branded PDF offer letters, dispatching, and joining-date confirmation tracking.
* **Monetization & Paid Access Control:** Implementation of the pay-per-access recruiter dashboard, locking deep video insights and AI analysis behind secure payment gateways.

---


## 🏗️ High-Level Repository Structure
```text
zecpath_ai_core/
│
├── /parsers/              # Phase 1: ATS & Resume Parsing Engine
├── /screening_ai/         # Phase 2: Voice API & Screening Logic
├── /interview_ai/         # Phase 3: Advanced HR Psychological Evaluator
├── /technical_ai/         # Phase 7: Multi-domain Tech Sandbox
├── /behavior_ai/          # Phase 8: Engagement & Focus Telemetry
├── /integrity_ai/         # Phase 9: Anti-Cheat & Proctoring Gates
├── /machine_test/         # Phase 10: Practical Code Evaluation
├── /aggregation_core/     # Phase 11: Unified Scoring Brain (Variance Engine)
├── /recommendation_core/  # Phase 12: Decision CEO & Hard Gates
├── /reporting_core/       # Phase 13: XAI Markdown Dossier Generation
├── /security_core/        # Phase 15: RBAC & AES-256 Encryption
├── /docs/                 # Phase 22+: Enterprise Documentation & Audits
├── /tests/                # Automated QA & E2E Validation Scripts
├── PORTFOLIO_SUMMARY.md   # Final Lead Architect Portfolio
└── README.md              # Master System Overview
```

## 🗂️ System Documentation Hub
Because of the massive scale of this enterprise architecture, technical documentation is split by microservice. Click the links below to view the detailed architecture, file structures, and execution commands for each system:

### Phase 1 - 25: Core Microservices & Architecture
* ➡️ **[Phase 1: ATS & Document Intelligence](./parsers/README.md)**
* ➡️ **[Phase 2: Voice Screening AI & API](./screening_ai/README.md)**
* ➡️ **[Phase 3: Advanced HR Interview Architecture](./interview_ai/README.md)**
* ➡️ **[Phase 7: Technical Interview AI System](./technical_ai/README.md)**
* ➡️ **[Phase 8: Behavioral AI & Engagement Analysis](./behavior_ai/README.md)**
* ➡️ **[Phase 9: Integrity & Malpractice Detection](./integrity_ai/README.md)**
* ➡️ **[Phase 10: Machine Test Practical Evaluation](./machine_test/README.md)**
* ➡️ **[Phase 11: Cross-Round Aggregation Engine](./aggregation_core/README.md)**
* ➡️ **[Phase 12: Final Recommendation AI](./recommendation_core/README.md)**
* ➡️ **[Phase 13: Hiring Intelligence Report Generator](./reporting_core/README.md)**
* ➡️ **[Phase 14: System Optimization & Refinement](./optimization_core/README.md)**
* ➡️ **[Phase 15: Security & AI Governance](./security_core/README.md)**
* ➡️ **[Phase 16: Full System Simulation](./simulation_core/README.md)**
* ➡️ **[Phase 17: Debugging & System Stabilization](./stabilization_core/README.md)**
* ➡️ **[Phase 18: V2.0 Advanced Feature Architecture](./advanced_features_v2/ROADMAP_V2.md)**
* ➡️ **[Phase 19: API Architecture & Integration Planning](./api_integration/API_CONTRACT.md)**
* ➡️ **[Phase 20: Performance Tuning & Scalability](./performance_tuning/SCALABILITY_PLAN.md)**
* ➡️ **[Phase 21: AI Monitoring & Observability Blueprint](./observability_core/OBSERVABILITY_PLAN.md)**

### Phase 26 - 29: Executive Commercial Handoff Assets
* 🏆 **[Lead Developer Internship Portfolio](./PORTFOLIO_SUMMARY.md)**
* 🚀 **[v2.0 Future Scaling Roadmap](./docs/11_AI_ROADMAP.md)**
* 🐛 **[Bug Fix & Optimization Audit (v1.0 Release)](./docs/09_BUG_FIX_REPORT.md)**
* ✅ **[Final System Validation Sign-off](./docs/10_SYSTEM_VALIDATION.md)**
* 🎤 **[Mock Demo & Contingency Plans](./docs/07_MOCK_DEMO_REPORT.md)**
* 📊 **Executive Presentation Deck:** [`/End-to-End-Intelligent-Recruitment-System.pdf`](./End-to-End-Intelligent-Recruitment-System.pdf)

---

## 🚀 Global Setup & Installation

**1. Clone the repository**
```bash
git clone [https://github.com/Murthaja-ai/zecpath_ai_core.git](https://github.com/Murthaja-ai/zecpath_ai_core.git)
cd zecpath_ai_core
```

**2. Create and activate a Virtual Environment**
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
pip install sentence-transformers torch flask pytest
```

**4. Run Production Engine Tests**
```bash
python -m pytest tests/test_release.py
```