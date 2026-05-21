# Phase 2: Voice Screening AI & API

## 📌 Overview
The Voice Screening AI is the autonomous interviewer for the Zecpath platform. It processes raw audio, transcribes speech with noise calibration, extracts intent via strict Pydantic schemas, evaluates technical and behavioral answers mathematically, handles real-world chaos (bad audio/language mixing), and serves the results via a Flask API.

## 🏗️ Core Architecture (Days 22 - 32)
* **Dataset Architecture (Days 22-23):** Designed a centralized, AI-ready JSON "Brain" and Pydantic-powered validation firewall.
* **Audio Ingestion Engine (Day 24):** STT pipeline with dynamic ambient noise calibration and a Regex NLP normalizer.
* **Answer Understanding Engine (Day 25):** HR Intent Classifier wrapped in strict Pydantic validation to extract Skills, Salary, and Availability.
* **Screening Scoring Engine (Day 26):** Mathematical grading rubric evaluating Clarity, Relevance, Completeness, and Consistency.
* **Behavioral EQ & Sentiment Engine (Day 27):** Uses lexical dictionaries and pacing logic to calculate Confidence and soft-skill metrics.
* **Report Generator (Day 28):** Aggregates technical scores and behavioral data into an Executive Summary JSON.
* **Conversation State Machine (Day 29):** Graph-based routing to manage live conversation flow and retry nodes.
* **System Optimization (Day 30):** Adjusted thresholds and built lightweight intent-mapping heuristics to reduce false rejections.
* **Chaos Engineering (Day 31):** Environmental resilience layers, Regex-based noise sanitizers, and hardware-confidence fallback routers.
* **API Finalization (Day 32):** Built a RESTful Flask API and mock E2E demo for enterprise frontend integration.

## 📂 Screening AI File Structure
zecpath_ai_core/
├── screening_ai/              
│   ├── audio_processor.py
│   ├── transcript_cleaner.py
│   ├── transcript_normalizer.py
│   ├── answer_engine.py
│   ├── intent_classifier.py
│   ├── improved_intent.py
│   ├── scoring_engine.py
│   ├── behavioral_engine.py
│   ├── report_generator.py
│   ├── report_exporter.py
│   ├── conversation_engine.py
│   ├── optimized_flow_updates.py
│   ├── robust_flow.py         
│   ├── noise_handler.py       
│   ├── error_handling.py
│   ├── error_framework.py     
│   ├── conversation_flow.json
│   └── screening_data_structure.json
├── models/                    
│   ├── transcript_validator.py
│   ├── understanding_validator.py
│   ├── scoring_validator.py
│   └── behavioral_validator.py
├── api/
│   └── routes.py              
├── demo/
│   └── run_demo.py            
├── tests/                     
│   ├── simulate_screening.py
│   ├── test_edge_cases.py
│   ├── test_behavior.py
│   └── test_report_generator.py

## 🌐 API Contract & Execution
Run these scripts from the root directory:

**1. Run End-to-End Showcase:**
`python demo/run_demo.py`

**2. Start API Web Server:**
`python api/routes.py` (Boots up the Flask Server on Port 5000)

**Endpoint:** `POST /screening/start`
**Payload Requirements:** Requires `candidate_id`, `job_id`, `answers`, `scores`, and `behavior` objects.
**Response:** Returns a fully structured JSON evaluation report including `final_score`, `decision`, and an executive `summary`.