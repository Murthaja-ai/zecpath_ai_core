# Dynamic Follow-Up Logic – Zecpath AI

## Objective
To enable adaptive and intelligent questioning based on candidate responses, moving the system from a static script to a dynamic psychological evaluation.

## Key Features
| Feature | Description |
| :--- | :--- |
| **Answer Quality Detection** | Identifies weak, basic, or strong responses. |
| **Follow-Up Generation** | Triggers Clarification, Examples, or Probing prompts. |
| **Difficulty Adaptation** | Adjusts the depth of the *next* question dynamically based on current performance. |
| **State Tracking** | Utilizes an OOP `InterviewState` class to log history and mathematically prevent question repetition. |

## Follow-Up Types
| Type | Trigger |
| :--- | :--- |
| **Clarification** | Unclear or uncertain answers ("I guess", "Maybe"). |
| **Elaboration** | Short answers (< 4 words). |
| **Example-based** | Basic answers (< 8 words). |
| **No Follow-Up** | Strong, complete answers. |

## Difficulty Modes (Next Question)
| Mode | Trigger | Result |
| :--- | :--- | :--- |
| **Simplify** | Low-quality past answer | Breaks the next question down into simpler terms. |
| **Example** | Medium past answer | Demands real-world proof for the next question. |
| **Advanced** | Strong past answer + High Confidence | Unlocks complex scenario framing for the next question. |
| **Normal** | Baseline | Standard question delivery. |

## System Flow (Decision Tree)
1. Ask Base Question.
2. Capture Answer & Confidence Score.
3. Analyze Answer Quality (`followup_engine.py`).
4. Generate Immediate Follow-up (if needed).
5. Adapt Difficulty Mode for the Next Question (`adaptive_engine.py`).
6. Update `InterviewState` to prevent repeating the base question.