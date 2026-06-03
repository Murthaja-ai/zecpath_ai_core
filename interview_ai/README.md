# Zecpath Advanced Interview AI

## 📌 Phase 3: Advanced HR Interview AI
Phase 3 conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture, actively listens to candidates, grades their soft skills, and compiles a comprehensive hiring report.

* **Dynamic Questioning & Empathy (Days 33-34):** Routes questions by persona and dynamically pushes back on weak answers using an `InterviewState` tracker.
* **Communication Evaluator (Day 35):** Objective NLP rubric grading Fluency, Grammar, and Vocabulary.
* **Psychological Profiler (Day 36):** Mathematical engine scoring delivery confidence, pacing, and stress indicators.
* **HR Scoring Engine (Day 37):** Master aggregator using role-based weights to generate a final 0-100 score and hiring decision.

---

## 🧠 Phase 4: Cognitive & Aptitude Evaluation
Phase 4 evolves the AI from testing *how* candidates speak to testing *how they think*. It introduces Situational Judgment Tests (SJTs) and generates final executive summaries.

* **Aptitude & Logic Engine (Day 38):** A heuristic grading model evaluating structured thinking, risk awareness, and scenario alignment.
* **Executive Summary Generator (Day 39):** A natural language processing (NLP) module that translates raw data from Phase 3 and Phase 4 into a structured, readable HR briefing, actively flagging critical behavioral risks.

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
    │   ├── summary_generator.py    # Day 39: Executive NLP briefing generator
    │   └── README.md              
    ├── docs/
    │   ├── Day33_HR_Interview_Design.md  
    │   ├── Day34_Adaptive_Logic.md       
    │   ├── Day35_Communication_Rubric.md 
    │   ├── Day35_Sample_Scores.json      
    │   ├── Day36_Behavioral_Rubric.md    
    │   ├── Day36_Sample_Behavior.json    
    │   ├── Day37_Scoring_Rubric.md       
    │   ├── Day37_HR_Report.json          
    │   ├── Day38_Aptitude_Rubric.md      
    │   ├── Day39_Reporting_Architecture.md # Day 39: Summary architecture logic
    │   └── Day39_Summary_Template.json     # Day 39: Final summary API contract
    └── tests/
        ├── test_day34_followup.py        
        ├── test_day35_communication.py   
        ├── test_day36_behavior.py        
        ├── test_day37_hr_scoring.py      
        ├── test_day38_aptitude.py        
        └── test_day39_summary.py         # Day 39: NLP generation and flag testing

## 💻 Execution Modules
Run these scripts from the root directory to test the engines:

**1. Test the Executive Summary Generator:**
`python tests/test_day39_summary.py`

**2. Test the Master HR Report:**
`python tests/test_day37_hr_scoring.py`

**3. Test the Aptitude & Logic Engine:**
`python tests/test_day38_aptitude.py`