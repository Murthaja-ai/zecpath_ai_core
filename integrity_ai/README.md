# Phase 9: Integrity & Malpractice Detection Shield

## 1. System Vision
The Integrity Module acts as Zecpath’s proactive compliance and security engine. By collecting sandboxed interaction events from the browser container alongside audio spectrum anomalies, the system detects cheating attempts while ensuring zero exposure to intrusive client-side spyware.

## 2. Structural Security Controls
To prevent false evaluations, security thresholds are bound directly to the active interview state provided by the Phase 7 Technical System and Phase 8 Behavioral System:

    [Live Telemetry Feed] ---> [Integrity Engine Pipeline] <--- [Context Overrides (JSON)]
                                         |
                                         v
                          [Compounding Anomaly Modifier Check]
                                         |
                                         +---> Score < 50? ---> [SILENT RECRUITER FLAG]
                                         +---> Threshold Over? -> [REALTIME USER WARNING]

## 3. Core Signal Definitions
* **Tab Switching:** Monitored via standard browser blur/focus event loops to detect if the candidate is searching for answers in a new window.
* **Loss of Screen Focus:** Calculated via the HTML5 Page Visibility API to detect minimized windows or background app usage.
* **External Voice Detection:** Handled via local WebAudio API frequency parsing to catch off-screen whispering or external assistance.
* **Gaze Deviation:** Fed directly via incoming coordinates computed by the Behavioral AI.

## 4. Anti-Bias & Privacy-First Safety Rules
* **Context Overrides:** Gaze limitations are dynamically relaxed by up to 300% during architectural whiteboarding or complex system design tasks.
* **Compounding Heuristics:** A single mistake (like an accidental tab switch) decays over time. The system only flags candidates when anomalies cluster together (e.g., Tab Switch + Focus Loss simultaneously).
* **Non-Intrusive Isolation:** The system operates securely within standard web browser sandbox boundaries—never requesting file system visibility, local machine administrative control, or screen-recording capabilities.