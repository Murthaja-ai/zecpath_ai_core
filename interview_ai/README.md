# Phase 3: Advanced HR Interview AI

## 📌 Overview
The Advanced HR Interview Engine is Phase 3 of the Zecpath hiring funnel. Unlike the quick 5-minute screening caller, this engine conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture—generating personalized interview questions based on the candidate's experience level, role, and real-time answer quality.

## 🏗️ Core Architecture (Day 33 - 35)
* **HR Interview Engine Design (Day 33):** 4-phase interview state machine (Intro, Core, Role-Based, Closing).
* **Question Bank Architecture (Day 33):** Decoupled JSON database categorized by persona and domain.
* **Follow-Up Detection Engine (Day 34):** Analyzes incoming answers to classify quality and triggers targeted empathy prompts.
* **Difficulty Adaptation Framework (Day 34):** Dynamically adjusts the psychological framing of the *next* question based on current performance.
* **OOP State Tracking (Day 34):** Uses an `InterviewState` class to prevent repetitive questioning.
* **Communication Evaluation Engine (Day 35):** An objective, heuristic NLP rubric that grades a candidate's Fluency, Grammar, Vocabulary, Clarity, and Structure on a normalized 0-100 scale while mathematically penalizing filler words.

## 📂 Interview AI File Structure

    zecpath_ai_core/
    ├── interview_ai/              
    │   ├── question_bank.json     
    │   ├── question_generator.py  
    │   ├── followup_engine.py     
    │   ├── adaptive_engine.py     
    │   ├── state_tracker.py       
    │   ├── communication_engine.py # Day 35: Objective grading heuristics
    │   ├── normalization.py        # Day 35: Mathematical bias-reduction
    │   └── README.md              
    ├── docs/
    │   ├── Day33_HR_Interview_Design.md  
    │   ├── Day34_Adaptive_Logic.md       
    │   ├── Day35_Communication_Rubric.md # Day 35: Scoring formula & rules
    │   └── Day35_Sample_Scores.json      # Day 35: Benchmark examples
    └── tests/
        ├── test_day34_followup.py        
        └── test_day35_communication.py   # Day 35: Evaluator unit tests

## 💻 Execution Modules
Run these scripts from the root directory to test the engines:

**1. Test the Dynamic Question Playlist:**

    python interview_ai/question_generator.py

**2. Test the Adaptive State Pipeline (Follow-ups & Adaptation):**

    python interview_ai/state_tracker.py

**3. Run Automated Unit Tests (Follow-up & Communication):**

    python tests/test_day34_followup.py
    python tests/test_day35_communication.py