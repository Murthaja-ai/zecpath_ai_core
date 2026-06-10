# Phase 7: Technical Interview AI System

## 1. Interview Flow Design Diagram

```text
[START]
   |
   v
[Phase 1: Introduction & PII Scrubbing]
   |
   v
[Phase 2: Experience Detection] -> Sets Initial State (Basic/Inter/Adv)
   |
   v
[Phase 3: Conceptual Probing]
   |
   v
[Difficulty Hysteresis Engine] (Loops based on streak performance)
   |
   v
[Phase 4: Scenario / Architecture Probing]
   |
   v
[Phase 5: Veto Security Check]
   |
   v
[Phase 6: Unified Scoring Export]
   |
   v
[END]
```

## 2. Interview State Structure (Live Tracking)
During an active interview, the system maintains this state matrix in memory to track momentum and adjust difficulty:

{
  "candidate_id": "C-2001",
  "role": "frontend_developer",
  "experience_band": "3-5",
  "current_difficulty": "intermediate",
  "positive_streak_count": 1,
  "negative_streak_count": 0,
  "questions_asked": [
    "Explain CSS Grid vs Flexbox with a real-world scenario."
  ],
  "status": "in_progress"
}

## 3. Sample Final Output
When the interview concludes, the Technical AI passes this standardized JSON packet to the Phase 5 Grand Unifier for the final hiring decision:

{
  "candidate_id": "C-2001",
  "technical_score": 82.5,
  "strengths": [
    "Strong Angular state management", 
    "Excellent UI/UX optimization"
  ],
  "weaknesses": [
    "System design knowledge limited regarding Webpack scaling"
  ],
  "security_veto_triggered": false,
  "technical_decision": "Strong Technical Alignment"
}