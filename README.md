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

## 📂 Repository Structure
```text
zecpath_ai_core/
├── docs/
│   └── api_specification.md   # REST API contracts & integration flow
│   └── qa_testing_report.md   # Day 17 Accuracy Metrics & v2 Backlog
│   └── performance_optimization_report.md # Day 18 Scaling upgrades
│   ├── system_architecture.md         # Day 19 Pipeline diagram & scoring logic
│   └── developer_guide.md             # Day 19 Setup & troubleshooting
│   └── final_evaluation_report.md     #  Day 20 Executive summary & portfolio piece
├── data/
│   ├── processed/             # Structured JSON outputs & Accuracy Reports
│   ├── schemas/               # Pydantic/JSON validation schemas
│   ├── skills_db.json         # Master taxonomy
│   └── master_jobs_db.json    # Normalized database of 67 FinTech Roles
├── parsers/
│   ├── parser_engine_v2.py    # Core text extraction logic
│   ├── resume_segmenter.py    # Document slicing logic
│   ├── skill_extractor.py     # Skill matching and confidence scoring
│   ├── experience_parser.py   # Datetime and duration NLP logic
│   ├── relevance_engine.py    # Algorithmic scoring matrix for past roles
│   ├── education_parser.py    # Degree and certification extraction
│   └── semantic_engine.py     # Vector embeddings and Cosine Similarity math
├── master_orchestrator.py # V2.0 Final Scoring & Output Generator
├── tests/                 # Unit tests and automated QA reports
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