# Zecpath HR Interview AI – System Architecture Specification
**Version:** 2.1.0-PROD  
**Author:** Murthaja Afham, Lead AI Architect  

---

## 1. High-Level Engineering Topology

The Zecpath Core operates as a highly modular, asynchronous pipeline written entirely in Python. The system functions between the client-facing Frontend layer and the persistent Data layer, using strict internal pipelines to process voice transcripts, optimize metrics, protect applicant privacy, and compute cross-round hiring decisions.

       [ CLIENT FRONTEND INTERFACE ]
                     │
         HTTPS REST  │  (JSON Payloads)
                     ▼
       ┌───────────────────────────────┐
       │   FastAPI Gateway Router      │
       └─────────────┬─────────────────┘
                     │
                     ▼
       ┌───────────────────────────────┐
       │  Ethics & Compliance Engine   │◀── [Data Striping / PII Masking]
       └─────────────┬─────────────────┘
                     │
                     ▼
       ┌───────────────────────────────┐
       │  Stability & Text Optimizer   │◀── [Filler Pruning / Cap Enforcer]
       └─────────────┬─────────────────┘
                     │
                     ▼
       ┌───────────────────────────────┐
       │  Conversational Soft Skills   │◀── [Adaptive / Behavioral Blocks]
       └─────────────┬─────────────────┘
                     │
                     ▼
       ┌───────────────────────────────┐
       │   Unified Scoring Engine      │◀── [Veto Logic / Cross-Round Fusion]
       └─────────────┬─────────────────┘
                     │
                     ▼
       ┌───────────────────────────────┐
       │   Database Persistence Layer  │◀── [90-Day GDPR Digital Shredder]
       └───────────────────────────────┘

---

## 2. Core Architectural Subsystems

1. **Ingestion & Masking Edge (`compliance_engine.py`):** Intercepts raw speech transcripts. Strips explicit names and maps binary identity markers to gender-neutral structures (`they/them`) prior to routing to analysis layers.
2. **Text Normalization Stack (`stability_optimizer.py`):** Mitigates text-processing volatility. Filters language filler anomalies, implements execution string loop caps, and maps boundaries to safe numerical scales.
3. **Conversational Engine Stack (`adaptive_engine.py` / `followup_engine.py`):** Directs the context-aware candidate playlist. Generates adaptive situational pushback requests if a user gives shallow inputs.
4. **Unified Scoring Matrix (`unified_scoring_engine.py`):** Consolidates historical, multi-round technical inputs with immediate behavioral features. Evaluates dealbreaker thresholds.

---

## 3. Mathematical Execution Framework

The Zecpath platform separates evaluation into distinct algorithmic phases before generating an immutable unified hiring score.

### Phase A: Conversational Soft-Skills Formulation
The native score for the interactive human resources evaluation block (S_HR) is computed via a weighted matrix of distinct linguistic and behavioral vectors:

S_HR = (V_rel * W_rel) + (V_comm * W_comm) + (V_conf * W_conf) + (V_cons * W_cons)

Where:
* V_rel = Textual relevance to target operational questions.
* V_comm = Language fluency, structural grammar, and lexical diversity.
* V_conf = Delivery confidence score mapped through conversational performance indexes.
* V_cons = Integrity score measuring consistency across early and late responses.
* Sum of Weights (W) = 1.0 (Contextually scaled by technical track parameters).

### Phase B: Cross-Round Unified Scaling (The Grand Unifier)
The final hiring score (S_Final) fuses the outputs of all multi-round technical evaluations, historical screening assessments, and immediate interview modules:

S_Final = Phi * [ (S_ATS * 0.30) + (S_Screening * 0.30) + (S_HR * 0.40) ]

### The Strategic Dealbreaker Multiplier (Phi)
The system contains a binary switch variable, Phi, known as the **Master Veto Modifier**. 
* Under standard operating conditions, Phi = 1.0.
* If the automated tracking system registers any system dealbreaker (e.g., severe ethics failure, critical security flags, or zero comprehension markers), Phi is instantly set to 0.0.

This mathematical constraint ensures that no matter how exceptional a candidate scores on a single metric, a security or regulatory failure instantly resets the absolute evaluation output to 0, preventing high-risk applicants from progressing.