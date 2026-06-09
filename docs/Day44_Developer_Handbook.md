# HR AI Interview Engine – Developer Handbook
**System Context:** Core Integration, Incident Mitigation, and QA Controls  

---

## 1. Quick-Start Integration Guide

To connect a new front-end layout or system client to the Zecpath AI Core pipeline, implement this standard communication loop:

[Client Startup] ──▶ Send POST /start to register Session
                        │
                        ▼
             Loop: Prompt Question to User
                        │
                        ▼
             Capture Audio/Speech Stream Input
                        │
                        ▼
             Send POST /answer containing raw data payload
                        │
                        ▼
             Process response parameters (Follow-up loops)
                        │
                        ▼
[Interview End]  ──▶ Send GET /report to surface calculated KPIs

---

## 2. Technical Operational Failure Modes & Mitigation Matrices

When managing server loops, network interfaces, or runtime environments, check this dictionary of system errors and resolution paths:

| Error Payload Code | Root System Cause | Immediate Mitigation Protocol |
| :--- | :--- | :--- |
| `INVALID_SESSION_TOKEN` | The requested `session_id` is missing or has expired. | Re-route the application pipeline to initiate a clean `/start` handshake. |
| `DATA_MINIMIZATION_LOCK` | Client requested access to a record older than 90 days. | Reject the request. The data retention lifecycle layer has permanently shredded this transcript row under GDPR guidelines. |
| `STT_TRANSLATION_VOLATILITY` | Raw text stream contains over 40% verbal filler syntax or noise. | Route the text payload through the `stability_optimizer.py` line module to normalize features before grading. |
| `VETO_OVERRIDE_TRIGGERED` | Candidate triggered critical security or competency flags. | System drops absolute score to zero. Do not re-run calculations; retain raw metrics for legal audit paths. |

---

## 3. Comprehensive Verification Testing Automation

To ensure changes to endpoints do not break our data formatting contracts, run the integration test harness from your local testing pipeline. The test file is located at `tests/test_day44_integration.py`.

Run this verification tool locally by executing the following terminal command from the root package repository:
`pytest tests/test_day44_integration.py`