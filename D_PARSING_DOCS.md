# 📄 Day 6: Job Description (JD) Parsing System Documentation

## 1. Objective
The purpose of the JD Parsing System is to ingest unstructured, human-written job descriptions and convert them into a standardized, AI-readable JSON format. This structured data is the prerequisite for the Day 7 ATS Scoring Engine.

---

## 2. System Architecture & Step-by-Step Workflow

The parsing engine (`jd_parser.py`) processes documents through a strict 5-step pipeline:

### Step 1: Text Normalization (The "Janitor" Phase)
* **What it does:** Reads the raw text and passes it through `text_cleaner.py`.
* **Technical Details:** Removes non-ASCII characters, normalizes weird bullet points (`•`, `➤` to `-`), and fixes horizontal spacing issues while preserving vertical line breaks.
* **Why it matters:** Prevents downstream regex rules from breaking due to hidden formatting artifacts.

### Step 2: Core Information Extraction (Regex Matching)
* **What it does:** Locates and extracts the non-negotiable job parameters.
* **Technical Details:**
  * **Job Title:** Uses `re.search` to find strings following "Job Title:".
  * **Experience:** Uses a complex Regex pattern `(\d+)(?:\s*-\s*(\d+))?` to extract exact integers (e.g., converting "3-5 years" into `min_years: 3` and `max_years: 5`).
  * **Education:** Scans for keywords like "Bachelor's", "B.S.", or "Master's" and maps them to standard strings.

### Step 3: Section Segmentation (Contextual Splitting)
* **What it does:** Slices the document into two distinct halves based on keyword triggers.
* **Technical Details:** Splits the text at the phrase "Nice to Have" (case-insensitive).
* **Why it matters:** Allows the AI to understand the *context* of a skill. A skill found in the top half is categorized as a strict requirement; a skill in the bottom half is a bonus.

### Step 4: The Synonym Engine (Skill Normalization)
* **What it does:** Translates HR jargon into standardized technical terms.
* **Technical Details:** The engine loops through the split text and checks it against `synonyms_db.json`. It uses word boundary Regex (`\b`) to ensure exact matches.
* **Example:** If the JD asks for "ML", the engine maps it to "Machine Learning" to ensure the candidate matching system doesn't unfairly penalize a candidate.

### Step 5: JSON Generation & Export
* **What it does:** Packages the extracted data into the Day 4 `job_description_schema.json` structure.
* **Output Location:** Saves the finalized file to `data/processed/sample_jd_parsed.json`.

---

## 3. Configuration & Maintenance

### Updating the Skill Dictionary
To add new skills or synonyms without modifying the core Python code:
1. Open `data/synonyms_db.json`.
2. Add the official skill as the Key, and an array of variations as the Value.
   ```json
   "NodeJS": ["Node.js", "NodeJS", "Node"]