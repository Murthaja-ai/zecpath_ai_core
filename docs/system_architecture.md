# 🏛️ Zecpath ATS - System Architecture & Scoring Logic

## 1. High-Level Architecture (The Pipeline)
The Zecpath ATS operates on a sequential, memory-optimized pipeline. Data flows from raw files to scored JSONs using generator-based batching to maintain 1% RAM usage.

    [Raw Resumes & JDs] 
           │
           ▼
    ┌──────────────────────┐
    │ 1. Parser Engine     │ (PyMuPDF, python-docx, Spacy)
    │ - Extracts Text      │ -> Outputs: cleaned_text
    │ - Cleans OCR Noise   │
    └──────────┬───────────┘
               ▼
    ┌──────────────────────┐
    │ 2. Section Segmenter │ (Regex, Keyword Matching)
    │ - Slices headers     │ -> Outputs: experience, education, skills
    └──────────┬───────────┘
               ▼
    ┌──────────────────────┐
    │ 3. Semantic Engine   │ (sentence-transformers, @lru_cache)
    │ - AI Vector Math     │ -> Outputs: semantic_similarity_score
    └──────────┬───────────┘
               ▼
    ┌──────────────────────┐
    │ 4. Master Scorer     │ (Dynamic Weighting Matrix)
    │ - Calculates Total   │ -> Outputs: final_ats_score
    └──────────────────────┘

## 2. The Core Scoring Logic
The ATS does not use hardcoded math. It uses a **Dynamic Role-Based Weighting System**. The engine calculates 4 isolated sub-scores and multiplies them by a predefined weight based on the seniority of the role.

**Sub-Score Calculations:**
1. **Skill Gap Score:** Uses Cosine Similarity (Threshold > 0.50) to match candidate skills against JD skills.
2. **Experience Score:** Calculated based on raw Years of Experience (YOE) vs JD requirements. Overqualification penalties apply for Senior candidates applying to Junior roles.
3. **Education Score:** Binary or partial scoring based on degree relevance (e.g., MSc = 1.0, BSc = 0.5).
4. **Project Score:** Keyword semantic match on the candidate's portfolio section.

**Example Weighting Matrix (Mid-Level Role):**
* Skills: 40%
* Experience: 30%
* Projects: 20%
* Education: 10%