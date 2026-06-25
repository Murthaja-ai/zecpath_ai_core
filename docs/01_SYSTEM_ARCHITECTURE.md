# Zecpath AI: Enterprise System Architecture

## 1. The Global Flow
Zecpath is not a single script; it is a distributed, horizontally scalable microservice architecture. Data enters through a secure gateway, is intelligently routed based on computational weight, and is permanently locked into a cryptographic ledger.

## 2. The 4-Tier Infrastructure

### Tier 1: Security & Gateway
* **JWT & API Key Middleware:** No request touches the AI without passing through the Gateway. The system strips HTTP headers and validates the JSON Web Token (JWT) to ensure the user is authenticated. 
* **PII-Masking Interceptor:** Before any data is processed, the Telemetry Logger utilizes Regex to find and mask Personally Identifiable Information (PII), such as converting emails to `[MASKED_EMAIL]`, ensuring strict EU AI Act and GDPR compliance.

### Tier 2: The Routing Layer
* **Sync Routing (The Fast Lane):** Lightweight text payloads (e.g., Live Interview Answers) are routed directly to the AI Engine for real-time (sub-50ms) grading.
* **Async Routing (The Heavy Lane):** Massive payloads (e.g., 10-page PDFs) are intercepted by the `async_webhook_handler`. The Gateway instantly returns a `PROCESSING` status to prevent the frontend UI from freezing, while the payload is pushed to an AWS SQS background queue.

### Tier 3: The AI Microservices
* **ATS Document Engine:** Extracts semantic skill graphs from resumes.
* **Voice & HR Screening:** Conducts dynamic, state-machine driven behavioral interviews.
* **Technical Sandbox:** Evaluates live code and system design architecture.

### Tier 4: Storage & Legal Vault
* **MongoDB:** Stores dynamic candidate states and temporary metadata.
* **AWS S3:** Stores raw PDF artifacts and MP3 audio logs.
* **The Cryptographic Vault:** The final AI hiring decision is processed through a SHA-256 algorithm, creating an immutable blockchain ledger to protect against legal claims of hiring bias.