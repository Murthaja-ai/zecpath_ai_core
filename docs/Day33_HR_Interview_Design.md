# HR Interview Engine Design – Zecpath AI

## Objective
To design a structured, highly intelligent AI-driven HR interview system that transitions from static screening scripts to dynamic, persona-based psychological evaluations.

## System Architecture Diagram

    ┌──────────────────────────┐
    │   Frontend (Web/App)     │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │   Backend API Layer      │
    └────────────┬─────────────┘
                 │
                 ▼
    ┌──────────────────────────────────────────────┐
    │ HR Interview AI Engine                       │
    │                                              │
    │ ┌───────────────────────────────────────┐    │
    │ │ Question Generator                    │    │
    │ │ - Role-based                          │    │
    │ │ - Experience-based                    │    │
    │ └───────────────────────────────────────┘    │
    │                                              │
    │ ┌───────────────────────────────────────┐    │
    │ │ Conversation Engine                   │    │
    │ │ - State machine                       │    │
    │ │ - Phase control                       │    │
    │ └───────────────────────────────────────┘    │
    │                                              │
    │ ┌───────────────────────────────────────┐    │
    │ │ Response Processing Engine            │    │
    │ │ - Intent detection                    │    │
    │ │ - Answer structuring                  │    │
    │ └───────────────────────────────────────┘    │
    │                                              │
    │ ┌───────────────────────────────────────┐    │
    │ │ Evaluation Engine                     │    │
    │ │ - Communication scoring               │    │
    │ │ - HR scoring                          │    │
    │ └───────────────────────────────────────┘    │
    │                                              │
    │ ┌───────────────────────────────────────┐    │
    │ │ Report Generator                      │    │
    │ │ - Summary                             │    │
    │ │ - Strengths / Risks                   │    │
    │ └───────────────────────────────────────┘    │
    └──────────────────────────────────────────────┘
                 │
                 ▼
    ┌──────────────────────────┐
    │   Database / Storage     │
    └──────────────────────────┘

## Key Components

| Component | Description |
| :--- | :--- |
| **Question Generator** | Dynamically assembles a unique question playlist based on role and experience. |
| **Conversation Engine** | Manages interview flow across 4 distinct psychological phases. |
| **Response Processor** | Structures and sanitizes candidate answers. |
| **Follow-Up Logic** | Evaluates answer depth in real-time to trigger elaboration prompts. |

## Interview Phases (The State Machine)

To mimic human HR psychology, the interview is strictly segmented into phases:

1. **Introduction Phase:** Warm-up and candidate comfort (e.g., "Tell me about yourself").
2. **Core HR Phase:** Deep behavioral mapping (Strengths, Weaknesses, Teamwork, Goals).
3. **Role-Based Phase:** Specific evaluations (Technical vs Non-Technical alignments).
4. **Closing Phase:** Dealbreakers (Availability, Notice Period, Final remarks).

## Personalization Logic

The AI adapts its approach based on three factors:

* **Experience Level:** Alters question depth (Fresher vs Experienced).
* **Role Type:** Alters domain focus (Technical vs Non-technical).
* **Answer Quality:** Short or uncertain answers trigger the `followup_logic.py` engine to dig deeper.

## Advantages

* **Dynamic Interviews:** Candidates cannot memorize a static script; every interview is uniquely generated.
* **Role-based Evaluation:** Prevents asking deep system architecture questions to a junior UI designer.
* **Scalability:** New questions can be added to the JSON database without touching the Python logic.