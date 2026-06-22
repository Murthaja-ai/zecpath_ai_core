# Zecpath AI Core: Phase 21 Observability & Audit Blueprint

## 1. Executive Summary
To ensure 99.9% uptime and strict legal compliance (GDPR/EU AI Act), the Zecpath AI Core utilizes a 3-tier Observability Architecture. We have abandoned basic text logging in favor of structured, PII-masked JSON telemetry, correlation-based distributed tracing, and cryptographic hashing for AI hiring decisions.

## 2. Telemetry & Tracing Architecture
* **PII-Masking Filter:** All incoming data is scrubbed against Regex patterns before logging. Emails and Phone numbers are automatically replaced with `[MASKED_EMAIL]` to prevent GDPR violations in log aggregators (Datadog/Splunk).
* **Correlation IDs:** Every API request is assigned a unique `req_uuid`. As a candidate's data travels from the ATS Server to the AI Interview Server to the Database, this ID remains constant, allowing engineers to trace exactly where a failure occurred in a microservice environment.

## 3. Cryptographic Audit Vault (Legal Defense)
* AI hiring decisions are no longer stored as simple database rows. 
* Every final decision (Selected/Rejected) generates a **SHA-256 cryptographic hash**, binding the candidate's scores to a timestamp and the previous record.
* This creates a blockchain-style immutable ledger. If an auditor requests proof of unbiased hiring, we can mathematically prove our records have not been tampered with post-decision.

## 4. Critical Alerting Thresholds
Automated Slack/PagerDuty alerts will trigger under the following conditions:
* **Latency Alert:** If `avg_processing_time` > `1.5s` for 3 consecutive minutes.
* **Failure Alert:** If `HTTP 500 Error Rate` > `2%` of total traffic.
* **Security Alert:** If `403 Forbidden` spikes > `50` per minute (indicates an active cyber attack or brute-force API key attempt).

## 5. Mission Control Dashboard Structure
* **Top Row (Business Health):** Total Processed Today | Live Interviews Active | Global Success Rate
* **Middle Row (System Health):** P99 API Latency | Current CPU Load per Microservice | Queue Depth (Async SQS)
* **Bottom Row (Security & AI):** Blocked Malpractice Attempts | Live Telemetry Errors | Audit Vault Status