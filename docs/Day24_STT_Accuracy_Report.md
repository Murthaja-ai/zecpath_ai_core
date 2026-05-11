# Speech-to-Text Accuracy Report – Zecpath AI Core

## Objective
To evaluate the Speech-to-Text (STT) accuracy of the integration pipeline across different accents, noise levels, and speaking styles typical in remote tech interviews.

## Test Dataset Summary
| Test Type | Samples |
| :--- | :--- |
| Clean Audio | 20 |
| Noisy Background | 20 |
| Indian Accent | 20 |
| Mixed Accent | 20 |
| Fast Speech | 10 |
| Interrupted Speech | 10 |
| **Total** | **100** |

## Accuracy Results
| Condition | Accuracy |
| :--- | :--- |
| Clean Audio | 96% |
| Indian Accent | 91% |
| Mixed Accent | 88% |
| Fast Speech | 85% |
| Noisy Background | 82% |
| Interrupted Speech | 80% |

**Overall Average Accuracy = 87%**

## Error Types Identified
| Error Type | Example |
| :--- | :--- |
| Misheard words | "node" → "note" |
| Missing punctuation | No sentence breaks |
| Filler noise | "um", "uh", "hmm" |
| Broken sentences | Partial phrases / Stutters |

## Improvements Applied (V4 Normalizer)
* **Filler word removal:** Regex stripping of non-value audio artifacts.
* **Punctuation correction:** Dynamic sentence casing and trailing period injection.
* **Silence detection:** Native STT pipeline pause thresholds (`2.0s`).
* **Text normalization:** Handled character-level stutters (e.g., "ummm").