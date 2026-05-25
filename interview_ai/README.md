# Phase 3: Advanced HR Interview AI

## 📌 Overview
The Advanced HR Interview Engine is Phase 3 of the Zecpath hiring funnel. Unlike the quick 5-minute screening caller, this engine conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture—generating personalized interview questions based on the candidate's experience level, role, and real-time answer quality.

## 🏗️ Core Architecture (Day 33 - 34)
* **HR Interview Engine Design (Day 33):** Designed the foundational architecture for the 4-phase interview state machine (Intro, Core, Role-Based, Closing).
* **Question Bank Architecture (Day 33):** Decoupled interview questions from Python logic into a scalable JSON database categorized by persona and domain.
* **Follow-Up Detection Engine (Day 34):** Analyzes incoming answers mathematically to classify quality (Empty, Too Short, Uncertain, Basic, Good) and triggers targeted empathy prompts (Clarification, Elaboration, Example-based).
* **Difficulty Adaptation Framework (Day 34):** Dynamically adjusts the psychological framing of the *next* question based on current performance (e.g., simplifying questions for struggling candidates, or throwing complex scenarios at confident ones).
* **OOP State Tracking (Day 34):** Uses an `InterviewState` class to maintain a live history of the conversation, using mathematical sets to completely prevent repetitive questioning.

## 📂 Interview AI File Structure

    zecpath_ai_core/
    ├── interview_ai/              
    │   ├── question_bank.json     # Decoupled database of behavioral/tech questions
    │   ├── question_generator.py  # Playlist compiler (Persona/Role routing)
    │   ├── followup_engine.py     # Answer quality detection & immediate follow-ups
    │   ├── adaptive_engine.py     # Difficulty adaptation for upcoming questions
    │   ├── state_tracker.py       # OOP memory tracker & Master pipeline integration
    │   └── README.md              # Phase 3 Documentation
    ├── docs/
    │   ├── Day33_HR_Interview_Design.md  # ASCII Architecture Diagram & Flow Design
    │   └── Day34_Adaptive_Logic.md       # Adaptive Decision Tree & Logic Rules
    └── tests/
        └── test_day34_followup.py        # Automated unit tests for logic validation

## 💻 Execution Modules
Run these scripts from the root directory to test the dynamic generation engines:

**1. Test the Dynamic Question Playlist:**

    python interview_ai/question_generator.py

**2. Test the Adaptive State Pipeline (Follow-ups & Adaptation):**

    python interview_ai/state_tracker.py

**3. Run Automated Unit Tests:**

    python tests/test_day34_followup.py