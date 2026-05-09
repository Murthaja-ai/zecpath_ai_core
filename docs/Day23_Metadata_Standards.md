# Transcript Metadata Standards – Zecpath AI Core

## Objective
To define the strict metadata standards required to convert voice-based screening conversations into structured, AI-processable, and auditable data.

## Core Metadata Fields
| Field Name | Description | Data Type |
| :--- | :--- | :--- |
| `transcript_id` | Unique transcript identifier | String (UUID) |
| `candidate_id` | Unique candidate ID linking to the ATS profile | String |
| `job_id` | Associated job ID for the applied role | String |
| `question_id` | Reference to the Day 22 master question bank | String |
| `duration_seconds` | Total length of the candidate's audio answer | Integer |
| `confidence_score` | Speech-to-text accuracy rating (0.0 to 1.0) | Float |
| `language` | Spoken language detected (e.g., 'en', 'hi') | String |
| `created_at` | UTC Timestamp of record creation | Datetime |

## Metadata Design Principles
1. **Consistency:** All transcripts, regardless of language, follow the exact same JSON and SQL structure enforced by Pydantic validation.
2. **Traceability:** Every single answer is permanently linked to a specific question ID and candidate ID.
3. **Auditability:** Raw text and audio confidence scores are preserved before normalization to prevent AI hallucinations from altering the legal record.
4. **Scalability:** The architecture natively supports multi-language and multi-round interviews.