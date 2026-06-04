# Zecpath Advanced Interview AI

## 📌 Phase 3: Advanced HR Interview AI
Phase 3 conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture, actively listens to candidates, grades their soft skills, and compiles a comprehensive hiring report.

* **Dynamic Questioning & Empathy (Days 33-34):** Routes questions by persona and dynamically pushes back on weak answers.
* **Communication Evaluator (Day 35):** Objective NLP rubric grading Fluency, Grammar, and Vocabulary.
* **Psychological Profiler (Day 36):** Mathematical engine scoring delivery confidence, pacing, and stress indicators.
* **HR Scoring Engine (Day 37):** Master aggregator generating a final 0-100 score and hiring decision.

---

## 🧠 Phase 4: Cognitive Evaluation & QA Simulation
Phase 4 tests how candidates think under pressure and provides the enterprise End-to-End (E2E) testing framework to guarantee the AI's safety and accuracy.

* **Aptitude & Logic Engine (Day 38):** A heuristic grading model evaluating structured thinking, risk awareness, and scenario alignment.
* **Executive Summary Generator (Day 39):** An NLP module translating raw data into a structured, readable HR briefing.
* **Mass QA Simulation Harness (Day 40):** An E2E testing architecture that simulates high-volume applicant loads (40+ candidates) across diverse psychological personas to prove mathematical stability and prevent scoring bias.

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
    │   └── README.md              
    ├── docs/
    │   ├── Day39_Reporting_Architecture.md 
    │   ├── Day39_Summary_Template.json     
    │   └── Day40_Simulation_Report.md      # Day 40: Master E2E QA and Phase 5 Recommendations
    └── tests/
        ├── test_day37_hr_scoring.py      
        ├── test_day38_aptitude.py        
        ├── test_day39_summary.py         
        └── hr_simulation.py              # Day 40: The 40-candidate E2E mass simulator

## 💻 Execution Modules
Run these scripts from the root directory to test the engines:

**1. Run the Full 40-Candidate E2E QA Simulation:**
`python tests/hr_simulation.py`

**2. Test Individual AI Components:**
`python tests/test_day39_summary.py`
`python tests/test_day38_aptitude.py`