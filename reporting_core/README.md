# Phase 13: Hiring Intelligence Report Generator

## 1. System Vision
The Reporting Core acts as the "Executive Assistant" of the Zecpath platform. It is responsible for compiling raw, multi-phase telemetry into a unified, human-readable dossier. It transforms machine-readable JSON into an export-ready format optimized for recruiter UI dashboards.

## 2. Core Architecture
This module resolves the "Dangling Logic" and "Data Disconnection" vulnerabilities found in standard report generators:

* **`report_compiler.py` (The Aggregator):** Safely ingests the exact outputs from the Phase 11 Aggregator and the Phase 12 Decision Brain. It does *not* recalculate thresholds; it acts as a pure aggregator to preserve data integrity and prevent scoring contradictions.
* **`report_formatter.py` (The Presenter):** Utilizes BLUF (Bottom Line Up Front) architecture. It structures the data into a Markdown dossier, pushing the Final Recommendation, Confidence Index, and AI Rationale to the absolute top of the document to save HR managers time.