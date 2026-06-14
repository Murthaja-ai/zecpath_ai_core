# Phase 11: Cross-Round Aggregation Engine

## 1. System Vision
The Aggregation Engine acts as the central intelligence hub of Zecpath. It reaches across all individual evaluation modules (ATS, Voice Screening, HR Interview, Technical Theory, and Machine Test) to synthesize a single, unified Hiring Fit Score.

## 2. Core Architecture
This module resolves critical mathematical flaws found in standard weighted-average calculators:

* **`weights_config.json`:** Decouples grading weights from the codebase, allowing HR to define dynamic evaluation matrices based on specific roles (e.g., heavily weighting communication for Sales, but heavily weighting coding for Engineers).
* **`calculation_engine.py`:** * **Cohort Normalization:** Replaces raw clamping with Min-Max scaling, adjusting candidate scores against historical difficulty distributions.
    * **Dynamic Residual Re-weighting:** Mathematically handles incomplete candidate profiles by proportionally redistributing the weight of missing rounds across active rounds, preventing false negatives.
* **`master_orchestrator.py`:** Generates Explainable AI (XAI) text summaries and standardizes the Decision/Fit boundaries to eliminate UI contradictions.