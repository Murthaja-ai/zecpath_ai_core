# Phase 10: Machine Test Practical Evaluation Engine

## 1. System Vision
The Machine Test module transitions the Zecpath AI from theoretical questioning to practical execution. It evaluates a candidate's live coding, debugging, and system design skills within an isolated sandbox environment. 

## 2. Core Architecture
Unlike primitive coding platforms that use rigid, pass/fail time limits, Phase 10 utilizes **Continuous Mathematical Decay** and **Task-Adaptive Thresholds**. 

* **`task_schema.json`**: Decouples evaluation rules from the Python logic. It defines distinct expectations for four core task types (Coding Problems, Debugging, File Tasks, and System Design).
* **`evaluation_engine.py`**: Calculates the technical score. It evaluates Code Quality via structural analysis (presence of functions/error handling) rather than simple line-counting, and scales runtime efficiency dynamically.
* **`scoring_pipeline.py`**: The master orchestrator. It aggregates the 80/20 Technical/Time split and interfaces with the Phase 9 Integrity Shield.

## 3. The Integrity Interlock
This module is strictly bound to Phase 9. If a candidate achieves a perfect practical score but triggers a multi-signal malpractice flag (Integrity Score < 50%), the Scoring Pipeline automatically intercepts the payload, nullifies the technical score to `0.0`, and outputs a `Disqualified` HR flag.