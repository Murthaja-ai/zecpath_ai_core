# 📄 Day 6: Job Description (JD) Parsing System Documentation

## 1. Objective
To ingest unstructured, human-written job descriptions (from PDFs or text files) and convert them into a standardized, AI-readable JSON Master Database.

---

## 2. System Architecture & Step-by-Step Workflow

The parsing pipeline processes documents through a highly automated 6-step pipeline:

### Step 1: The Auto-Splitter (Data Ingestion)
* **What it does:** Reads a master corporate PDF catalog.
* **Technical Details:** Uses `pdfplumber` to extract text and a highly forgiving Regular Expression knife (`re.split`) to slice the document into dozens of distinct job text files, safely saving them to `data/raw_jds/`.

### Step 2: Text Normalization
* **What it does:** Cleans the raw text.
* **Technical Details:** Removes non-ASCII characters and fixes hidden formatting artifacts (like invisible Unicode characters) to prevent downstream regex rules from breaking.

### Step 3: Core Information Extraction
* **What it does:** Extracts non-negotiable parameters like Experience and Education.
* **Technical Details:** Uses advanced Regex to extract exact integers for experience (e.g., "3-5 years" becomes `min: 3, max: 5`) and flags domain-specific degrees (e.g., CFA, CA, MBA, Bachelor's in Finance).

### Step 4: Section Segmentation
* **What it does:** Slices the document based on requirement strictness.
* **Technical Details:** Splits the text at the phrase "Nice to Have". Skills in the top half are categorized as mandatory; skills in the bottom half are bonuses.

### Step 5: The Synonym Engine (Skill Normalization)
* **What it does:** Translates HR jargon into standardized technical terms using `synonyms_db.json`.
* **Technical Details:** Uses word boundary Regex (`\b`) to ensure exact matches. If the JD asks for "DCF", the engine maps it to the standardized skill "Valuation".

### Step 6: Master Database Aggregation
* **What it does:** Compiles all parsed jobs into a single queryable file.
* **Output Location:** Saves the finalized array of all jobs to `data/processed/master_jobs_db.json`.

---

## 3. Configuration & Maintenance

### Updating the Skill Dictionary
To add new skills or synonyms without modifying the core Python code:
1. Open `data/synonyms_db.json`.
2. Add the official skill as the Key, and an array of variations as the Value.
   ```json
   "Valuation": ["valuation", "valuations", "DCF", "intrinsic value", "P/E"]