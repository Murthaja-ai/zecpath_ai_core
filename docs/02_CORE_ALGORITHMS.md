# Zecpath AI: Core Algorithms & Scoring Logic

## 1. The Fallacy of Averages
Zecpath does not use basic additive scoring (e.g., `Score = A + B`). Simple averages reward candidates who memorize one specific skill but fail in all others. Instead, Zecpath uses a **Dynamic Variance Engine**.

## 2. The Standard Deviation Penalty
When aggregating the Technical, HR, and ATS scores, the AI calculates the mathematical variance between the domains. 
* If a candidate scores `[90, 80, 85]`, they receive a high final score because they are well-rounded.
* If a candidate scores `[100, 40, 95]`, the Variance Engine applies a steep Standard Deviation penalty. The system recognizes this candidate is highly volatile and flags them as a risk.

## 3. The LRU Memory Cache
To prevent the server from recalculating heavy standard deviation math for thousands of applicants, the scoring engine is wrapped in an `@lru_cache`. If the engine detects a mathematical array it has solved previously, it pulls the answer directly from RAM, reducing CPU latency by over 98%.

## 4. Hard Gate Overrides (The Integrity Shield)
Zecpath enforces strict, non-negotiable Hard Gates that override all numerical scores:
* **The Cheating Interlock:** If the Phase 9 Behavioral AI detects continuous off-screen eye focus or tab-switching, the Integrity Risk flag is triggered. The candidate's technical score is immediately zeroed out, regardless of how perfectly they coded the answer.
* **The Consent Gate:** If the `legal_consent_granted` flag is missing from the API payload, the AI refuses to process the data, throwing a `451 Unavailable For Legal Reasons` error.