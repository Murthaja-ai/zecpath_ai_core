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

## 📂 Repository Structure
```text
zecpath_ai_core/
├── data/
│   ├── processed/         # Structured JSON outputs & Accuracy Reports
│   ├── schemas/           # Pydantic/JSON validation schemas
│   ├── skills_db.json     # Master taxonomy
│   └── master_jobs_db.json# Normalized database of 67 FinTech Roles
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