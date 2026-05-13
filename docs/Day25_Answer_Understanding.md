# Answer Intent & Understanding Engine – Zecpath AI Core

## Objective
To interpret candidate responses and extract meaningful structured information for AI evaluation.

## Key Features

### 1. Intent Classification
* **Identifies purpose of answer**
* **Categories:**
  * Introduction
  * Skills
  * Experience
  * Salary
  * Availability

### 2. Entity Extraction
| Entity | Extracted |
| :--- | :--- |
| Skills | ✔ |
| Experience | ✔ |
| Salary | ✔ |
| Availability | ✔ |

### 3. Response Quality Checks
* Off-topic detection
* Vague answer detection
* Missing answer detection

### 4. Structured Output
* Converts unstructured text → AI-ready JSON
* Enables mathematical scoring and evaluation

## Analysis
* **Advantages:** Enables deeper understanding of answers, reduces manual HR effort, and improves screening accuracy.
* **Limitations:** Currently relies on rule-based intent detection (Regex) resulting in limited context understanding.
* **Future Improvements:** Implement ML-based intent classification, context-aware understanding, and LLM-powered semantic parsing.