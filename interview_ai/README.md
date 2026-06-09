# Zecpath Advanced Interview AI

## 📌 Phase 3: Advanced HR Interview AI
Conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture, actively listens to candidates, grades soft skills, and compiles a hiring report.

* **Dynamic Questioning & Empathy (Days 33-34):** Routes questions by persona and dynamically pushes back on weak answers.
* **Communication Evaluator (Day 35):** Objective NLP rubric grading Fluency, Grammar, and Vocabulary.
* **Psychological Profiler (Day 36):** Mathematical engine scoring delivery confidence, pacing, and stress indicators.
* **HR Scoring Engine (Day 37):** Master aggregator generating a final 0-100 score and hiring decision.

---

## 🧠 Phase 4: Cognitive Evaluation & QA Simulation
Tests how candidates think under pressure and provides the enterprise End-to-End (E2E) testing framework to guarantee the AI's safety and accuracy.

* **Aptitude & Logic Engine (Day 38):** A heuristic grading model evaluating structured thinking, risk awareness, and scenario alignment.
* **Executive Summary Generator (Day 39):** An NLP module translating raw data into a structured, readable HR briefing.
* **Mass QA Simulation Harness (Day 40):** An E2E testing architecture that simulates high-volume applicant loads (40+ candidates) across diverse psychological personas to prove mathematical stability and prevent scoring bias.

---

## 🚀 Phase 5: The Grand Unifier, System Optimization & Compliance
Phase 5 connects all previous Zecpath modules (ATS, Screening, Deep Interview) into a single, commercial-ready product optimized for precision, enterprise scaling, and strict legal compliance.

* **Unified Scoring Engine (Day 41):** The master algorithm that ingests scores from Phase 1, 2, and 4. It applies role-based dynamic weights and enforces strict "Dealbreaker Vetoes" to output a single 0-100% Hiring Fit score.
* **Optimization & Stability Suite (Day 42):** Eliminates mathematical and text processing volatility. Uses absolute boundary scaling to remove score spikes, extracts metrics from conversational filler text, and locks conversational loop caps.
* **Ethics & Compliance Engine (Day 43):** Enforces global hiring regulations (GDPR, NYC AI Law). Actively strips PII/demographics before scoring, translates numerical outputs into plain-English justifications, and automatically purges stale candidate data.
* **System Integration & API (Day 44):** The enterprise handoff layer. Defines the REST API endpoints, JSON payloads, mathematical topologies, and developer onboarding protocols for frontend integration.

---

## 📂 Interview AI File Structure

    zecpath_ai_core/
    ├── interview_ai/              
    │   ├── question_bank.json     
    │   ├── aptitude_questions.json 
    │   ├── question_generator.py  
    │   ├── followup_engine.py     
    │   ├── adaptive_engine.py     
    │   ├── state_tracker.py       
    │   ├── communication_engine.py 
    │   ├── normalization.py        
    │   ├── behavioral_engine.py    
    │   ├── hr_scoring_engine.py    
    │   ├── aptitude_engine.py      
    │   ├── summary_generator.py    
    │   ├── unified_scoring_engine.py       # Day 41: Cross-round grand unifier with veto logic
    │   ├── stability_optimizer.py          # Day 42: Outlier smoothing & transcript metrics cleanup
    │   ├── compliance_engine.py            # Day 43: PII Masking & Data Retention Rules
    │   └── README.md              
    ├── docs/
    │   ├── Day39_Reporting_Architecture.md 
    │   ├── Day39_Summary_Template.json     
    │   ├── Day40_Simulation_Report.md      
    │   ├── Day41_Unified_Architecture.md   
    │   ├── Day41_Unified_Report.json       
    │   ├── Day42_Optimization_Report.md    
    │   ├── Day43_Compliance_Report.md      
    │   ├── Day44_Architecture_Spec.md      # Day 44: System topology and scoring formulas
    │   ├── Day44_API_Reference.json        # Day 44: OpenAPI/Swagger endpoint definitions
    │   └── Day44_Developer_Handbook.md     # Day 44: Integration manual and troubleshooting
    └── tests/
        ├── test_day37_hr_scoring.py      
        ├── test_day38_aptitude.py        
        ├── test_day39_summary.py         
        ├── hr_simulation.py              
        ├── test_day41_unified.py           
        ├── test_day42_stability.py         
        ├── test_day43_compliance.py        
        └── test_day44_integration.py       # Day 44: API payload and GDPR lifecycle mock testing

## 🧩 Core Engine Glossary

**Phase 3: Conversational & Soft Skills**
* `question_generator.py`: Ingests resume data and persona types to generate tailored opening questions.
* `followup_engine.py`: The dynamic listener; triggers pushback or clarification prompts if candidate answers are weak.
* `state_tracker.py`: The conversation's memory buffer; ensures the AI does not repeat questions or get stuck in loops.
* `communication_engine.py`: NLP rubric that grades transcript text for fluency, grammar, and vocabulary.
* `behavioral_engine.py`: Evaluates psychological stress, pacing, and confidence markers.
* `hr_scoring_engine.py`: Aggregates the Phase 3 modules into a final soft-skills score.

**Phase 4: Logic & Reporting**
* `aptitude_engine.py`: Evaluates structured thinking, risk awareness, and technical problem-solving logic.
* `summary_generator.py`: Translates numerical scoring arrays into plain-English executive HR summaries.

**Phase 5: Enterprise Unification & Safety**
* `unified_scoring_engine.py`: Fuses ATS, Screening, and Interview scores; applies role-based weights and dealbreaker vetoes.
* `stability_optimizer.py`: The QA layer; cleans transcripts of filler words and mathematically drops scoring anomalies.
* `compliance_engine.py`: The legal layer; masks PII/demographics for blind grading and enforces GDPR data deletion.

**Phase 6: Integration & Handoff**
* `Day44_Architecture_Spec.md`: The structural map and mathematical equations driving the backend.
* `Day44_API_Reference.json`: The strict REST API contract mapping out endpoints for the frontend team.
* `Day44_Developer_Handbook.md`: The onboarding guide containing setup flows and error resolution matrices.

---

## 💻 Execution Modules
Run these scripts from the root directory to test the engines:

**1. Test API Endpoints & GDPR Purging:**
`pytest tests/test_day44_integration.py`

**2. Test Compliance, Privacy, and Explainability:**
`python tests/test_day43_compliance.py`

**3. Test System Stability & Anomaly Filtering:**
`python tests/test_day42_stability.py`

**4. Test the Unified Scoring Engine (Veto & Math):**
`python tests/test_day41_unified.py`

**5. Run the Full 40-Candidate E2E QA Simulation:**
`python tests/hr_simulation.py`