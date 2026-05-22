# Phase 3: Advanced HR Interview AI

## 📌 Overview
The Advanced HR Interview Engine is Phase 3 of the Zecpath hiring funnel. Unlike the quick 5-minute screening caller, this engine conducts a deep, 30-minute psychological evaluation. It abandons static scripts in favor of a Dynamic Playlist Architecture—generating personalized interview questions based on the candidate's experience level, role, and real-time answer quality.

## 🏗️ Core Architecture (Day 33+)
* **HR Interview Engine Design (Day 33):** Designed the foundational architecture for the 4-phase interview state machine (Intro, Core, Role-Based, Closing).
* **Question Bank Architecture:** Decoupled interview questions from Python logic into a scalable JSON database categorized by persona and domain.
* **Role-Based Question Generator:** A dynamic engine that compiles a unique, randomized 6-question playlist tailored to whether the candidate is a Fresher/Experienced or Technical/Non-Technical.
* **Empathy & Follow-Up Logic:** Real-time heuristics that analyze answer length and confidence (e.g., detecting "I'm not sure") to dynamically trigger deeper elaboration prompts.

## 📂 Interview AI File Structure

    zecpath_ai_core/
    ├── interview_ai/              
    │   ├── question_bank.json     # Decoupled database of behavioral/tech questions
    │   ├── question_generator.py  # Playlist compiler (Persona/Role routing)
    │   ├── interview_state.json   # Real-time state machine tracker
    │   ├── followup_logic.py      # Empathy heuristics and elaboration triggers
    │   └── README.md              # Phase 3 Documentation
    ├── docs/
    │   └── Day33_HR_Interview_Design.md  # ASCII Architecture Diagram & Flow Design

## 💻 Execution Modules
Run these scripts from the root directory to test the dynamic generation engines:

**1. Test the Dynamic Question Playlist:**

    python interview_ai/question_generator.py

**2. Test the Empathy & Follow-up Trigger:**

    python interview_ai/followup_logic.py