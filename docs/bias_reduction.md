# 🛡️ Fairness, Normalization & Bias Reduction Strategy
**Zecpath ATS - Enterprise Governance Pipeline (Day 15)**

## 1. Objective
To enforce ethical hiring practices, ensure legal compliance (GDPR/EEOC), and standardize resume evaluation by intercepting algorithmic output before it reaches human recruiters.

## 2. Core Governance Modules

### A. The Blind Hiring Module (`anonymizer.py`)
Human recruiters are susceptible to Unconscious Bias based on names, age, and background. 
* **Action:** The system uses Consistent SHA-256 Hashing to convert names (e.g., "Alice") into irreversible, tracking-safe identifiers (e.g., `Candidate_93B2`).
* **Legal Compliance:** Strictly deletes fields prone to discrimination, including `gender`, `age`, `dob`, `marital_status`, and `nationality`.

### B. The Anti-Cheat Security Layer (`anti_cheat.py`)
Traditional ATS systems rely heavily on keyword matching, allowing dishonest candidates to "Keyword Stuff" their resumes with invisible text.
* **Action:** The system calculates the `Skill Density Ratio` (Total Skills / Total Words).
* **Penalty:** If technical keywords make up an abnormal percentage of the resume (e.g., >15%), the system flags the candidate for "Keyword Stuffing" and mathematically slashes their final score by 50%.

### C. Statistical Curve Grading (`normalizer.py`)
Strictly written Job Descriptions often result in artificially low scores across the entire candidate pool, causing recruiters to mistakenly reject top talent.
* **Action:** Implements Min-Max Normalization `(score - min) / (max - min)`.
* **Result:** Grades the candidate pool on a mathematical curve, ensuring the best relative candidate is presented at a 100% benchmark, providing recruiters with an intuitive 0-100 scale.