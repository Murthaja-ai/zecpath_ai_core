# Confidence & Sentiment Analysis – Zecpath AI Core

## Objective
To evaluate communication quality and behavioral signals during AI screening.

## Key Signals
| Signal | Description |
| :--- | :--- |
| **Hesitation** | Filler words & uncertainty |
| **Length** | Depth of response |
| **Pace** | Speaking speed (Words per Second) |
| **Sentiment** | Positive/Negative tone |
| **Uncertainty** | Lack of confidence |
| **Contradiction** | Logical inconsistency |

## Confidence Formula
> **Confidence** = (Length × 0.4) + (Pace × 0.4) + (1 - Hesitation × 0.2)

## Communication Strength Levels
| Score | Level |
| :--- | :--- |
| **≥ 0.75** | Strong |
| **0.50 – 0.74** | Moderate |
| **< 0.50** | Weak |

## Analysis
* **Advantages:** Captures behavioral signals, improves candidate evaluation, and adds human-like judgment.
* **Limitations:** Rule-based sentiment detection; no physical tone/audio pitch analysis yet.
* **Future Improvements:** Voice tone analysis, advanced emotion detection, and ML-based behavioral scoring.