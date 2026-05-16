# Zecpath AI Core - Autonomous Hiring Pipeline (FinTech Domain)

## 📌 Overview
Zecpath AI Core is a highly specialized NLP data pipeline designed to automate candidate screening and scoring. Recently refactored to focus on the **Quantitative Finance & FinTech domain**, this engine ingests unstructured resumes, segments the text, extracts technical skills via custom Knowledge Graphs, and calculates mathematically weighted experience relevance.

## 🏗️ Core Architecture (The Pipeline)
Our candidate processing is broken down into independent AI-driven microservices:

1. **Resume Segmentation Engine (Day 8):** Ingests raw PDFs/Docx and uses heuristic NLP to accurately slice the document into strict logical buckets (e.g., EXPERIENCE, EDUCATION, SKILLS).
2. **Skill Inference Engine (Day 9):** Cross-references extracted text against our FinTech `skills_db.json`. It maps human text to a custom knowledge graph, assigning mathematical confidence scores (0.0 - 1.0) to candidate capabilities.
3. **Experience Relevance Engine (Day 10):** A sophisticated time-series parser that calculates precise employment durations, detects overlapping jobs, flags employment gaps, and uses a Role Similarity Matrix to discount irrelevant past experience.
4. **Education & Certification Engine (Day 11):** Extracts academic credentials, standardizes degree hierarchies, and identifies high-value FinTech certifications.
5. **Semantic Matching Engine (Day 12):** The AI "Brain" of the ATS. Utilizes `sentence-transformers` to generate mathematical text embeddings. Performs semantic skill gap analysis and calculates a holistic candidate match score against specific Job Descriptions.
6. **Dynamic Scoring Framework (Day 13):** A configurable, rule-based engine that applies role-specific mathematical weights to raw scores, handles missing data gracefully, and generates legally defensible audit trails.
7. **Candidate Ranking & Shortlisting (Day 14):** An automated HR factory that sorts candidates, resolves tie-breakers, applies configurable threshold zones (Shortlist/Review/Reject), and exports recruiter-friendly CSV reports
8. **Enterprise Governance Pipeline (Day 15):** The final security and ethics layer. Implements PII anonymization for blind hiring, Min-Max statistical curve grading, and algorithmic anti-cheat detection for keyword stuffing.
9. **API Architecture & Integration (Day 16):** The RESTful API blueprint. Defines asynchronous job polling mechanics, request/response JSON schemas, rate-limiting security, and HTTP error standards for seamless frontend integration.
10. **QA & System Testing (Day 17):** Conducted rigorous precision/recall testing across diverse edge-case personas (Freshers, Senior Executives, Career Pivots) against human manual review to identify algorithm biases and generate a v2.0 improvement backlog.
11. **Production Optimization (Day 18):** Refactored the architecture for Enterprise scale. Implemented Multithreading for 10x faster PDF extraction, `@lru_cache` to eliminate redundant AI vector math, and Python Generators (`yield`) to maintain 1% flat memory usage across massive data batches.
12. **Knowledge Transfer (Day 19):** Drafted comprehensive Enterprise documentation, including system architecture diagrams, scoring logic breakdowns, and a developer troubleshooting guide to ensure team scalability and eliminate a Bus Factor of 1.
13. **Production Handover (Day 20):** Finalized the system for Enterprise deployment. Created a controlled synthetic dataset for secure live demonstrations and authored the Executive Evaluation Report summarizing the architecture, optimization, and business value of the ATS.
14. **Eligibility Decision Engine (Day 21):** The automated HR Gatekeeper. Applies strict business logic (location, experience constraints, mandatory skills) via decoupled JSON configurations. Features a Semantic Bridge to recognize AI-inferred skills and a 15-point mathematical grace period to safely flag borderline candidates for human review instead of auto-rejection.
15. **HR Screening Dataset Architecture (Day 22):** Designed a centralized, AI-ready JSON "Brain" for the automated Voice Interviewer. Replaced fragmented data files with a single structured dataset featuring conversational categorization, strict LLM listening directives (evaluation criteria, expected answer types), dynamic variable injection (targeting specific skill gaps identified in Day 21), and multilingual future-proofing (English, Hindi, Malayalam)
16. **Transcript Data Architecture (Day 23):** Designed the data pipeline to convert raw voice conversations into structured, AI-ready data. Implemented a Pydantic-powered validation firewall to protect database integrity, a Regex-based text NLP normalizer to clean messy human speech (filler words, trailing punctuation), and defined the SQL database schema for Enterprise storage.
17. **Audio Ingestion Engine (Day 24):** Built the STT (Speech-to-Text) ingestion pipeline. Implemented dynamic ambient noise calibration and native silence-detection to process raw `.wav` files. Integrated a V4 Regex Normalizer to handle character-level stutters ("ummm"), strip conversational fillers, and dynamically format final sentence punctuation for downstream LLM readability.
18. **Answer Understanding Engine (Day 25):** Implemented an HR Intent Classifier and Entity Extraction engine (Skills, Experience, Salary, Availability) wrapped in a strict Pydantic validation firewall. Built batch-processing capabilities and automated quality checks to flag off-topic, vague, or missing answers.
19. **Screening Scoring Engine (Day 26):** Engineered an unbiased, weighted mathematical grading rubric (The AI Judge). Evaluates transcripts based on Clarity (25%), Relevance (30%), Completeness (25%), and Consistency (20%). Features Explainable AI outputs and automated 'Pass/Review/Reject' logic.
20. **Behavioral EQ & Sentiment Engine (Day 27):** Built a behavioral analysis pipeline. Uses lexical dictionaries and pacing logic (Words per Second) to calculate Confidence and Sentiment out of 1.0. Outputs a final 'Strong/Moderate/Weak' Communication Strength indicator alongside psychological behavior flags.
21. **AI Screening Report Generator (Day 28):** Engineered the "Executive Summary" aggregation layer. Transforms raw technical scores and behavioral JSON into a recruiter-friendly format. Highlights critical dealbreakers (salary, availability) and generates automated text summaries for strengths, risks, and missing data. Includes a text-export module for offline reading.

## 📂 Repository Structure
```text
zecpath_ai_core/
├── docs/
│   ├── api_specification.md               # REST API contracts & integration flow
│   ├── qa_testing_report.md               # Day 17 Accuracy Metrics & v2 Backlog
│   ├── performance_optimization_report.md # Day 18 Scaling upgrades
│   ├── system_architecture.md             # Day 19 Pipeline diagram & scoring logic
│   ├── developer_guide.md                 # Day 19 Setup & troubleshooting
│   ├── final_evaluation_report.md         # Day 20 Executive summary & portfolio piece
│   ├── Day23_Metadata_Standards.md        # Transcript data rules and audit standards
│   ├── Day24_STT_Integration.md           # Day 24 STT pipeline blueprint
│   └── Day24_STT_Accuracy_Report.md       # Day 24 STT stress-test metrics (87% accuracy)
│   └── Day26_Scoring_Engine.md        # Day 26: Mathematical formulas and decision rules
│   └── Day27_Behavioral_Analysis.md   # Day 27: EQ, NLP lexicons, and soft-skill metrics
├── data/
│   ├── processed/             # Structured JSON outputs & Accuracy Reports
│   ├── demo_dataset/          
│   │   ├── eligibility_rules.json     # Day 21: Decoupled HR business logic configuration
│   │   └── screening_questions.json   # Day 22: Multilingual AI-ready interview script
│   ├── schemas/               # Pydantic/JSON validation schemas
│   │   └── transcript_schema.json     # Day 23: Turn-by-turn conversation blueprint
│   ├── database_schema.sql    # Day 23: PostgreSQL tables for transcript storage
│   ├── skills_db.json         # Master taxonomy
│   └── master_jobs_db.json    # Normalized database of 67 FinTech Roles
├── models/
│   └── transcript_validator.py# Day 23: Pydantic firewall for transcript data integrity
│   └── understanding_validator.py     # Day 25: Pydantic schema for extracted facts & flags
│   └── scoring_validator.py           # Day 26: Pydantic schema for the final Report Card
│   └── behavioral_validator.py        # Day 27: Pydantic schema for the EQ Profile
├── screening_ai/
│   ├── audio_processor.py             # Day 24: STT engine with silence & noise detection
│   ├── intent_classifier.py           # Day 25: Strict HR intent categories (Enum)
│   ├── answer_engine.py               # Day 25: Regex fact extraction & batch processor
│   ├── transcript_cleaner.py          # Day 24: Batch processor for multiple audio answers
│   ├── transcript_normalizer.py       # Day 23/24: Regex NLP cleaner (V4 with stutter & grammar fix)
│   └── screening_data_structure.json  # Day 23: Post-AI evaluation data structure
│   └── scoring_engine.py              # Day 26: Mathematical grading, weighting, and aggregation logic
│   └── behavioral_engine.py           # Day 27: NLP filler word detection and sentiment analysis
│   ├── report_generator.py            # Day 28: Aggregates tech, behavior, and raw answers into a UI-ready format
│   └── report_exporter.py             # Day 28: Converts JSON reports to printable Text format
├── parsers/
│   ├── eligibility_engine.py  # Day 21: Rule-based Gatekeeper with missing-data safety net
│   ├── parser_engine_v2.py    # Core text extraction logic
│   ├── resume_segmenter.py    # Document slicing logic
│   ├── skill_extractor.py     # Skill matching and confidence scoring
│   ├── experience_parser.py   # Datetime and duration NLP logic
│   ├── relevance_engine.py    # Algorithmic scoring matrix for past roles
│   ├── education_parser.py    # Degree and certification extraction
│   └── semantic_engine.py     # Vector embeddings and Cosine Similarity math
├── master_orchestrator.py # V2.0 Final Scoring & Output Generator
├── tests/                 # Unit tests and automated QA reports (incl. test_day23.py)
├── utils/                 # Logging and configuration modules
├── METADATA_STANDARDS.md  # Documentation for data normalization
├── PIPELINE_DIAGRAM.md    # Visual flow of the ATS processing
└── STORAGE_ARCHITECTURE.md# Polyglot storage design specs
```

## 🚀 Setup & Installation

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
pip install sentence-transformers torch
```

## 💻 Execution Modules
The pipeline is designed to be executed modularly for testing. Run the orchestrator scripts from the root directory:
* `python run_day8.py` -> Tests the Document Segmentation engine.
* `python run_day9.py` -> Tests the Skill Extraction & Confidence Scoring.
* `python run_day10.py` -> Tests the Timekeeper & Relevance Matrix.
* `python run_day11.py` -> Tests the Education & Certification Engine.
* `python run_day12_validation.py` -> Generates the Semantic Matching Accuracy Report.
* `python master_orchestrator.py` -> **Runs the full Enterprise Pipeline.**

## 🔐 Confidentiality Notice
This repository contains proprietary data engineering pipelines for the Zecpath platform. Please refer to NDA guidelines before replicating scoring logic or taxonomy databases.
