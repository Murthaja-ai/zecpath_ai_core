# Phase 1: ATS & Document Intelligence

## 📌 Overview
The ATS Engine handles the top of the Zecpath hiring funnel. It automatically parses unstructured resumes, maps extracted skills to a FinTech taxonomy, calculates precise employment durations, and uses Semantic NLP to rank candidates against specific Job Descriptions. It acts as the automated HR gatekeeper before triggering Voice AI interviews.

## 🏗️ Core Architecture (Days 1 - 21)
* **Days 1-7 (Foundation & Ingestion):** Environment setup, database schemas, and baseline PDF text extraction.
* **Resume Segmentation Engine (Day 8):** Uses heuristic NLP to slice documents into logical buckets (Experience, Skills, Education).
* **Skill Inference Engine (Day 9):** Cross-references text against `skills_db.json`. Maps text to a custom knowledge graph with confidence scores.
* **Experience Relevance Engine (Day 10):** Calculates employment durations, detects overlapping jobs, and flags gaps.
* **Education & Certification Engine (Day 11):** Standardizes degrees and identifies high-value certifications.
* **Semantic Matching Engine (Day 12):** Utilizes `sentence-transformers` for semantic skill gap analysis and calculates match scores.
* **Dynamic Scoring Framework (Day 13):** Applies role-specific mathematical weights to raw scores.
* **Candidate Ranking (Day 14):** Sorts candidates, resolves tie-breakers, and applies threshold zones.
* **Enterprise Governance (Day 15):** Implements PII anonymization for blind hiring and algorithmic anti-cheat detection.
* **Optimization & QA (Days 16-20):** Multithreading for 10x faster extraction, `@lru_cache` optimizations, and precision testing.
* **Eligibility Decision Engine (Day 21):** Enforces strict business logic (location, mandatory skills).

## 📂 ATS File Structure
```text
zecpath_ai_core/
├── parsers/                   
│   ├── eligibility_engine.py
│   ├── parser_engine_v2.py
│   ├── resume_segmenter.py
│   ├── skill_extractor.py
│   ├── experience_parser.py
│   ├── relevance_engine.py
│   ├── education_parser.py
│   ├── semantic_engine.py
│   ├── jd_parser.py
│   └── text_cleaner.py
├── utils/                     
│   ├── anonymizer.py
│   ├── anti_cheat.py
│   ├── normalizer.py
│   └── ranking_engine.py
├── schemas/                   
│   ├── job_description_schema.json
│   └── resume_schema.json
├── data/                      
│   ├── raw_jds/
│   ├── raw_resumes/
│   └── processed/
├── master_orchestrator.py     
└── run_day8.py -> run_day15.py
```

## 💻 Execution Modules
Run these scripts from the root directory to test the ATS pipeline:
* `python run_day8.py` -> Tests Document Segmentation.
* `python run_day9.py` -> Tests Skill Extraction.
* `python run_day12_validation.py` -> Generates the Semantic Matching Accuracy Report.
* `python master_orchestrator.py` -> Runs the full Enterprise ATS Pipeline.