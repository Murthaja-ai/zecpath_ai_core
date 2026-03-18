# Zecpath AI Core - Autonomous Hiring Pipeline (FinTech Domain)

## 📌 Overview
Zecpath AI Core is a highly specialized NLP data pipeline designed to automate candidate screening and scoring. Recently refactored to focus on the **Quantitative Finance & FinTech domain**, this engine ingests unstructured resumes, segments the text, extracts technical skills via custom Knowledge Graphs, and calculates mathematically weighted experience relevance.

## 🏗️ Core Architecture (The Pipeline)
Our candidate processing is broken down into independent AI-driven microservices:

1. **Resume Segmentation Engine (Day 8):** Ingests raw PDFs/Docx and uses heuristic NLP to accurately slice the document into strict logical buckets (e.g., EXPERIENCE, EDUCATION, SKILLS).
2. **Skill Inference Engine (Day 9):** Cross-references extracted text against our FinTech `skills_db.json`. It maps human text to a custom knowledge graph, assigning mathematical confidence scores (0.0 - 1.0) to candidate capabilities.
3. **Experience Relevance Engine (Day 10):** A sophisticated time-series parser that calculates precise employment durations, detects overlapping jobs (preventing double-counting), flags employment gaps, and uses a Role Similarity Matrix to discount irrelevant past experience against target FinTech roles.

## 📂 Repository Structure
'''
zecpath_ai_core/
├── data/
│   ├── processed/         # Structured JSON outputs (Scores, Parsed Profiles)
│   ├── schemas/           # Pydantic/JSON validation schemas for ATS data
│   ├── skills_db.json     # Master taxonomy of tech/finance skills
│   └── master_jobs_db.json# Normalized database of 67 FinTech Target Roles
├── parsers/
│   ├── parser_engine_v2.py    # Core text extraction logic
│   ├── resume_segmenter.py    # Document slicing logic
│   ├── skill_extractor.py     # Skill matching and confidence scoring
│   ├── experience_parser.py   # Datetime and duration NLP logic
│   └── relevance_engine.py    # Algorithmic scoring matrix for past roles
├── tests/                 # Unit tests and automated QA reports
├── utils/                 # Logging and configuration modules
├── METADATA_STANDARDS.md  # Documentation for data normalization
├── PIPELINE_DIAGRAM.md    # Visual flow of the ATS processing
└── STORAGE_ARCHITECTURE.md# Polyglot storage design specs
'''

## 🚀 Setup & Installation
1. Clone the repository
git clone https://github.com/Murthaja-ai/zecpath_ai_core.git
cd zecpath_ai_core

2. Create and activate a Virtual Environment
python -m venv venv
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt


## 💻 Execution Modules
The pipeline is designed to be executed modularly for testing. Run the orchestrator scripts from the root directory:
* python run_day8.py -> Tests the Document Segmentation engine.
* python run_day9.py -> Tests the Skill Extraction & Confidence Scoring.
* python run_day10.py -> Tests the Timekeeper & Relevance Matrix.

## 🔐 Confidentiality Notice
This repository contains proprietary data engineering pipelines for the Zecpath platform. Please refer to NDA guidelines before replicating scoring logic or taxonomy databases.
