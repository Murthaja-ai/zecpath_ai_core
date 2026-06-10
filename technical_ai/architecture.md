# Zecpath Technical Interview AI – System Blueprint
**Phase 7 Architecture | Adaptive State Machine**

## 1. System Objective
To conduct role-specific, adaptive technical interviews that dynamically adjust difficulty based on a strict Hysteresis (Streak) progression model, while maintaining Phase 5 compliance and veto security standards.

---

## 2. The Core Pipeline (Integration with Phase 5)
The Technical AI does not operate in isolation. It utilizes the existing HR architecture:
1. **Ingestion & Scrubbing:** Candidate data enters and is immediately routed through the `Compliance Engine` (Day 43) to strip PII.
2. **State Initialization:** The system calculates the starting difficulty based on the `Experience Router`.
3. **The Adaptive Loop:** The `Question Engine` fires, the candidate answers, the `Stability Optimizer` (Day 42) cleans the text, and the `Difficulty Engine` adjusts the state.
4. **Final Handoff:** Results are sent to the `Unified Scoring Engine` (Day 41) for a final hiring decision, subject to the Master Veto.

---

## 3. Interview Flow States (The 4 Phases)

### Phase 1: Introduction & Calibration
* **Trigger:** Session Start.
* **Action:** AI verifies candidate identity, scrubs PII, and asks a basic experience-related icebreaker.
* **Exit Condition:** 1 valid response recorded.

### Phase 2: Conceptual Exam (Theory)
* **Trigger:** Entry from Phase 1.
* **Action:** Rapid-fire theoretical questions based on the candidate's core stack (e.g., "Explain the JavaScript Event Loop").
* **Exit Condition:** Candidate answers 3 questions. System calculates a running baseline score.

### Phase 3: Scenario Probing (Applied Logic)
* **Trigger:** Entry from Phase 2.
* **Action:** AI presents a real-world debugging or architecture problem. Difficulty is dictated by Phase 2 performance.
* **Exit Condition:** Candidate completes 2 scenarios.

### Phase 4: System Design (Seniors Only)
* **Trigger:** Candidate experience > 5 years AND Phase 3 score > 70%.
* **Action:** AI asks a high-level scalability or infrastructure question.
* **Exit Condition:** 1 completed answer. Moves to Report Generation.

---

## 4. The "Hysteresis" Difficulty Progression Engine
*To prevent volatile "Yo-Yo" scoring, the AI requires a streak to change tiers.*

* **Initial State:** Set by Years of Experience (0-2 = Basic | 3-5 = Intermediate | 5+ = Advanced).
* **Level UP Trigger:** Candidate must score **> 80% on TWO consecutive questions** to move up a tier.
* **Level DOWN Trigger:** Candidate must score **< 40% on TWO consecutive questions** to drop a tier.
* **Cold-Start Protection:** A candidate cannot be dropped from their baseline tier until at least 2 questions have been asked, preventing drops due to initial nervousness.

---

## 5. Security & Dealbreaker Vetoes
If the candidate suggests an architecture that violates core security principles (e.g., storing passwords in plaintext, bypassing authorization checks), the Technical AI triggers the Phase 5 Master Veto (`CRITICAL_SECURITY_VIOLATION`), immediately ending the interview loop and forcing a `0.0` score.