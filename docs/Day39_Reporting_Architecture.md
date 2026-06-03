# Interview Summary Generator – Zecpath AI

## Objective
To convert the millions of data points generated during Phase 3 and Phase 4 into a 10-second, highly readable Executive Summary for human HR recruiters.

## Core Architectural Upgrades
* **Aptitude Integration:** Unlike standard AI reporting, Zecpath includes situational logic, risk awareness, and cognitive structure in its final briefing.
* **Single Source of Truth:** The Summary Generator does not perform primary math. It strictly consumes and averages the Master HR Report and the Master Aptitude Report.
* **Risk Flag Escalation:** The system explicitly elevates critical failures (like contradictions or backpedaling) to a dedicated `Risk Flags` array so recruiters never miss a toxic candidate trait.

## NLP (Natural Language Processing) Output
The system abandons robotic string concatenation in favor of fluid narrative generation, automatically adjusting the tone of the paragraph based on the severity of the detected risk flags.