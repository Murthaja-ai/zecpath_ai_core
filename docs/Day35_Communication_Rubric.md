# Communication Skill Evaluation – Zecpath AI

## Objective
To objectively evaluate candidate communication skills during AI interviews using a heuristic, rule-based NLP pipeline that eliminates human bias.

## The Master Scoring Formula
**Communication Score** = `(Fluency × 0.2) + (Grammar × 0.2) + (Vocabulary × 0.2) + (Clarity × 0.2) + (Structure × 0.2) − Filler Penalty`

## Parameter Definitions
| Parameter | Description | Evaluative Metric |
| :--- | :--- | :--- |
| **Fluency** | Sentence continuity | Counts valid sentences split by punctuation (`.`, `!`, `?`). |
| **Grammar** | Basic correctness | Checks for capital start letters and closing punctuation. |
| **Vocabulary** | Lexical diversity | Calculates the ratio of unique words vs total words. |
| **Clarity** | Understandability | Evaluates minimum word count thresholds. |
| **Structure** | Logical flow | Detects connective argument markers (e.g., "because"). |
| **Penalty** | Filler word deduction | Subtracts points for "um", "uh", "like", "literally". |

## Standardized Score Levels
| Score Range | Level Designation |
| :--- | :--- |
| **85 – 100** | Excellent |
| **70 – 84** | Good |
| **50 – 69** | Average |
| **0 – 49** | Poor |