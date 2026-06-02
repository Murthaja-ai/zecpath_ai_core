# HR Interview Final Scoring Engine – Zecpath AI

## Objective
To aggregate all communication, behavioral, and relevance metrics from the 30-minute interview into a single, explainable 0-100 hiring recommendation.

## Role-Based Weight Configurations
To ensure fairness, the AI dynamically adjusts its priorities based on the seniority of the candidate.

| Metric | Fresher Weight | Experienced Weight |
| :--- | :--- | :--- |
| **Relevance** | 25% | 40% (Technical accuracy is critical) |
| **Communication** | 35% | 20% |
| **Confidence** | 20% | 20% |
| **Consistency** | 20% | 20% |

## Decision Thresholds
* **75.0 – 100.0:** `STRONG HIRE`
* **55.0 – 74.9:** `CONSIDER` (Requires human review)
* **0.0 – 54.9:** `REJECT`

## Explainability
The engine translates raw mathematical numbers into human-readable sentences for the final HR Report, ensuring Hiring Managers understand exactly *why* points were deducted (e.g., "Displayed nervous pacing" vs "Strayed from the core prompt").