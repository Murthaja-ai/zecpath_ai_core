# Phase 8: Behavioral AI & Engagement Analysis

## 1. System Objective
The Behavioral AI module analyzes non-invasive visual telemetry (eye focus, head stability, engagement) to assess a candidate's focus and confidence. Unlike primitive systems, this engine is **Context-Aware**, dynamically shifting its scoring weights based on the current interview phase to protect candidates from false "distraction" flags during deep cognitive tasks.

## 2. The Context-Aware Analysis Framework

The system adjusts its strictness based on the live technical context:

| Interview Context | Eye Focus Weight | Penalty Strictness | Expected Candidate Behavior |
| :--- | :--- | :--- | :--- |
| **Introduction Phase** | 40% | Moderate | General eye contact and engagement. |
| **Conceptual Probing** | 50% | High | High screen focus to prevent off-screen reading. |
| **System Design Challenge**| 15% | Low | Allowed to look away to think or sketch. Focus is on engagement. |

## 3. Signal Pipeline & Execution Flow

```text
[START]
   |
   v
[Phase 1: Webcam Telemetry Capture] -> Outputs coordinates (0.0 to 1.0)
   |
   v
[Phase 2: Baseline Calibration] -> 120s phase to establish natural resting posture
   |
   v
[Phase 3: Contextual Rule Fetch] -> Queries `behavioral_schema.json` based on active question
   |
   v
[Phase 4: Dynamic Math Engine] -> Calculates positive signals minus context-weighted distraction
   |
   v
[Phase 5: Risk Tier Mapping] -> Maps final % to Low, Moderate, or High Risk insights
   |
   v
[END] -> Appends insight to Final Hiring Report