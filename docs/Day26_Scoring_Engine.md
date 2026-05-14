# Screening Scoring Engine – Zecpath AI Core

## Objective
To objectively evaluate candidate responses during AI screening interviews and eliminate human bias.

## Scoring Parameters
| Parameter | Description |
| :--- | :--- |
| **Clarity** | How clearly and confidently the candidate communicates (punishes vague/evasive answers). |
| **Relevance** | Alignment with the question's expected intent (punishes off-topic answers). |
| **Completeness** | Coverage of required details and hard facts (Skills, Experience, Availability). |
| **Consistency** | Logical answers free of contradictory, off-topic, or highly evasive indicators. |

## Scoring Formula
The engine normalizes scores out of 100 using the following weighted mathematical formula:
> **Final Score** = (Clarity × 0.25) + (Relevance × 0.30) + (Completeness × 0.25) + (Consistency × 0.20)

## Decision Rules
The final aggregated screening score dictates the automated hiring recommendation:
* **≥ 70.0** : `Pass`
* **50.0 – 69.9** : `Review`
* **< 50.0** : `Reject`

## Features
* **Per-question evaluation:** Granular scoring for every individual answer.
* **Aggregate scoring:** Summarized performance averages across the entire interview.
* **Explainable outputs:** AI generates human-readable text explaining exactly *why* a specific score was given.
* **Normalized scoring:** Flat 0-100 percentage scale for easy HR dashboard integration.

## Analysis
* **Advantages:** Standardized evaluation, completely transparent decision-making, and highly scalable for processing thousands of AI interviews.
* **Limitations:** Currently relies on rule-based scoring and basic text-length checks for clarity; limited deep semantic understanding.
* **Future Improvements:** Transition to ML-based scoring models, context-aware evaluation mapping against job descriptions, and behavioral signal integration (e.g., voice tone analysis).