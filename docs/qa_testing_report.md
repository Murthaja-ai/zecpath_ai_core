# 🧪 Zecpath ATS - QA & Accuracy Testing Report (Day 17)

## 1. Objective
To validate the accuracy, reliability, and role-adaptability of the Zecpath AI scoring engine by comparing AI-generated decisions against human manual review across diverse edge-case profiles.

## 2. Test Suite & Methodology
We tested a standard `Data Analyst` Job Description (requiring Python, SQL, and 2 years of experience) against 4 distinct candidate personas:
* **Candidate A:** The Ideal Tech Profile (3 YOE, Exact Skills)
* **Candidate B:** The Fresher (0 YOE, Great Academic Projects)
* **Candidate C:** The Senior Executive (15 YOE, Non-Technical Leadership)
* **Candidate D:** The Career Pivot (4 YOE, Non-Technical)

## 3. Human vs. AI Results
| Profile | Human Decision | AI Decision | Match? | AI Reasoning |
| :--- | :--- | :--- | :--- | :--- |
| **A. Ideal Tech** | Shortlist | Shortlist (92%) | ✅ Yes | Perfect alignment of semantic skills and experience duration. |
| **B. Fresher** | Shortlist | Reject (41%) | ❌ No | AI applied strict missing-data penalties for 0 YOE and ignored academic projects. |
| **C. Executive** | Review | Reject (28%) | ❌ No | AI applied a heavy Overqualification Penalty and found low semantic similarity for "Director of Sales". |
| **D. Career Pivot**| Reject | Reject (15%) | ✅ Yes | AI correctly identified 0 semantic technical skills. |

## 4. Accuracy Metrics & Confusion Matrix
Out of 4 edge-case tests, the system performed with strong precision but requires threshold tuning to improve recall.

* **True Positives (1):** Correctly shortlisted the Ideal Tech candidate.
* **True Negatives (1):** Correctly rejected the Non-Tech career pivot.
* **False Positives (0):** The AI successfully blocked unqualified candidates.
* **False Negatives (2):** The AI incorrectly rejected the Fresher and the Senior Executive due to overly strict configuration weights.

**Calculated Metrics:**
* **Accuracy:** 50% (2/4 correct decisions)
* **Precision:** 100% (No bad candidates were shortlisted)
* **Recall:** 33% (System is currently too aggressive with rejections)

## 5. Improvement Backlog (v2.0 Goals)
Based on these mismatches, the following updates are required for the next iteration of the scoring engine:
1. **The "Fresher" Configuration:** Create a specific `role_bucket` for entry-level roles that mathematically weights "Academic Projects" equally to "Work Experience" to prevent unfair rejections of recent graduates.
2. **Semantic Context for Seniority:** Adjust the Experience Relevance Engine so it doesn't penalize Senior Executives applying for mid-level roles, provided they possess the core technical requirements.