# Phase 3: Advanced HR Interview AI

## 📌 Overview
The Advanced HR Interview Engine is Phase 3 of the Zecpath hiring funnel. It conducts a deep, 30-minute psychological and technical evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture, actively listens to candidates, grades their soft skills, and compiles a comprehensive hiring report.

## 🏗️ Core Architecture (Days 33 - 37)
* **HR Interview Engine Design (Day 33):** 4-phase interview state machine (Intro, Core, Role-Based, Closing).
* **Question Bank Architecture (Day 33):** Decoupled JSON database categorized by persona and domain.
* **Follow-Up Detection Engine (Day 34):** Analyzes incoming answers to classify quality and triggers targeted empathy prompts.
* **Difficulty Adaptation Framework (Day 34):** Dynamically adjusts the psychological framing of the *next* question based on current performance.
* **OOP State Tracking (Day 34):** Uses an `InterviewState` class to prevent repetitive questioning.
* **Communication Evaluation Engine (Day 35):** Objective NLP rubric that grades Fluency, Grammar, Vocabulary, Clarity, and Structure.
* **Psychological & Behavioral Profiler (Day 36):** A mathematical engine scoring delivery confidence, emotional sentiment, and stress indicators.
* **HR Scoring & Report Engine (Day 37):** The master aggregator. It applies role-based weight configurations (Fresher vs. Experienced) to combine all metrics into a final 0-100 score, generating an explainable JSON report card and a final hiring decision (STRONG HIRE, CONSIDER, or REJECT).

## 📂 Interview AI File Structure

    zecpath_ai_core/
    ├── interview_ai/              
    │   ├── question_bank.json     
    │   ├── question_generator.py  
    │   ├── followup_engine.py     
    │   ├── adaptive_engine.py     
    │   ├── state_tracker.py       
    │   ├── communication_engine.py 
    │   ├── normalization.py        
    │   ├── behavioral_engine.py    
    │   ├── hr_scoring_engine.py    # Day 37: Master HR report aggregator
    │   └── README.md              
    ├── docs/
    │   ├── Day33_HR_Interview_Design.md  
    │   ├── Day34_Adaptive_Logic.md       
    │   ├── Day35_Communication_Rubric.md 
    │   ├── Day35_Sample_Scores.json      
    │   ├── Day36_Behavioral_Rubric.md    
    │   ├── Day36_Sample_Behavior.json    
    │   ├── Day37_Scoring_Rubric.md       # Day 37: Weight configs & decision rules
    │   └── Day37_HR_Report.json          # Day 37: Final API mock data
    └── tests/
        ├── test_day34_followup.py        
        ├── test_day35_communication.py   
        ├── test_day36_behavior.py        
        └── test_day37_hr_scoring.py      # Day 37: Aggregation and math validation

## 💻 Execution Modules
Run these scripts from the root directory to test the engines:

**1. Test the Master Final Report:**
`python tests/test_day37_hr_scoring.py`

**2. Test the Individual Sub-Engines:**
`python tests/test_day36_behavior.py`
`python tests/test_day35_communication.py`