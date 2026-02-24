# 🗄️ Zecpath ATS: Storage Architecture

## 1. Overview
To ensure scalability and fast query performance, the Zecpath ATS uses a polyglot persistence strategy. This means we use different types of databases optimized for specific types of data across the AI pipeline.

## 2. Storage Mapping

| Data Type | Storage Solution | Format | Reason for Choice |
| :--- | :--- | :--- | :--- |
| **Raw Resumes** | Cloud Object Storage (AWS S3) | `.pdf`, `.docx` | High-volume file storage. Accessed via secure, time-expiring URLs. |
| **Parsed AI Profiles** | Document Database (MongoDB) | `.json` / BSON | Highly flexible schema. Perfect for handling variable lengths of work experience and skills. |
| **Parsed Job Descriptions** | Document Database (MongoDB) | `.json` / BSON | Easily updatable and links directly to the AI scoring engine. |
| **ATS Match Scores** | Relational Database (PostgreSQL) | SQL Rows | Strict, tabular data. Allows HR dashboards to run fast sorting queries (e.g., `ORDER BY score DESC`). |
| **Screening Reports** | Relational Database (PostgreSQL) | SQL Rows | Links Candidate ID, Job ID, and final HR decisions using foreign keys. |
| **Interview Feedback** | Relational Database (PostgreSQL) | SQL Rows | Structured feedback (Score: 1-5) and text notes must be linked to the Candidate ID for final hiring decisions. |

## 3. Data Retention & Security
* **PII (Personally Identifiable Information):** Names, emails, and phone numbers are isolated from the main AI training databases to protect candidate privacy.
* **Archiving:** Raw PDFs are moved to cold storage (e.g., AWS S3 Glacier) 90 days after a job is closed to save server costs.
## 4. Model Versioning & Retraining Strategy
* **Versioning:** Every parsed document is tagged with the `model_version` (e.g., `v1.0`). If the parsing logic is updated, the version increments to `v1.1` to ensure data consistency.
* **Retraining Datasets:** High-quality resumes that result in successful hires will be anonymized (PII removed) and copied into a separate, secure "Training Data" AWS S3 Bucket. This data will be used to fine-tune future iterations of the Zecpath AI models.