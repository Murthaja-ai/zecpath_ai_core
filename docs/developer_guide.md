# 💻 Zecpath ATS - Developer & Troubleshooting Guide

## 1. Local Environment Setup
To get the Zecpath ATS running on a new machine, follow these steps strictly to avoid dependency conflicts.

1. **Clone the repository:** `git clone [repository_url]`
2. **Create a virtual environment:** `python -m venv venv`
3. **Activate the environment:**
   * Mac/Linux: `source venv/bin/activate`
   * Windows: `venv\Scripts\activate`
4. **Install core dependencies:** `pip install -r requirements.txt`
5. **Download the Spacy NLP Model (Required):** `python -m spacy download en_core_web_sm`

## 2. Core Project Structure
Understanding the repository layout is critical for extending the ATS.

    zecpath_ai_core/
    ├── data/
    │   ├── raw_resumes/         # Place input PDF/DOCX files here
    │   ├── processed/           # JSON outputs from the Parser Engine
    │   └── final_ats_scores.csv # The final generated enterprise report
    ├── docs/                    # Architecture, QA, and Performance documentation
    ├── parsers/
    │   ├── parser_engine_v2.py  # Multithreaded text extraction
    │   └── semantic_engine.py   # Cached AI vector matching
    └── master_orchestrator.py   # The main execution script (Generator based)

## 3. How to Run the Pipeline
Ensure your raw PDFs are in `data/raw_resumes/` and the target Job Description is loaded in the Orchestrator.

**Execution Command:**
`python master_orchestrator.py`

## 4. Troubleshooting & Known Issues

### Issue 1: `OSError: [E050] Can't find model 'en_core_web_sm'`
* **Cause:** The Spacy language model was not downloaded during setup.
* **Fix:** Run `python -m spacy download en_core_web_sm` in your terminal.

### Issue 2: `FileNotFoundError` during Batch Processing
* **Cause:** The pipeline cannot find the resumes or the Job Description JSON.
* **Fix:** Ensure you have placed files inside `data/raw_resumes/`. The orchestrator will automatically skip hidden files (like `.DS_Store`), but it requires at least one valid PDF to run.

### Issue 3: `MemoryError` or Server Crash during Execution
* **Cause:** The pipeline has been modified by a junior developer to use a standard `list` instead of the `yield` generator, causing massive RAM bloat.
* **Fix:** Check `master_orchestrator.py` and ensure `stream_candidates()` is using the `yield` keyword to stream files one by one.

### Issue 4: Extremely slow semantic processing (> 5 seconds per resume)
* **Cause:** The `@lru_cache` was removed, or multithreading was applied improperly to the AI model instead of the parser. 
* **Fix:** Ensure `semantic_engine.py` uses `@lru_cache(maxsize=10000)` and that the batch processing loops sequentially so threads can share the cache memory.