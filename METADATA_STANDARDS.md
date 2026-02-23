# 🏷️ Zecpath ATS: Metadata Standards

## 1. Overview
In order to maintain data integrity across the AI pipeline, every parsed document (Resume or Job Description) must be stamped with a standardized metadata object. This ensures we can track the lifecycle of a document from upload to final hiring decision.

## 2. Core Metadata Fields

| Field Name | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `candidate_id` | String (UUID) | Unique identifier linking the resume to the user's account in the main database. | `"cnd_8f72a9b"` |
| `job_id` | String (UUID) | Unique identifier for the specific job posting they applied to. | `"job_3391xpf"` |
| `timestamp` | ISO 8601 Date | The exact date and time the document was parsed by the AI. | `"2026-02-23T14:30:00Z"` |
| `model_version` | String | Tracks which version of the AI parsed this file, crucial for future retraining and debugging. | `"resume_parser_v1.0"` |
| `document_status` | String | Tracks the current phase of the file in the pipeline (e.g., uploaded, parsed, scored, rejected). | `"parsed"` |

## 3. JSON Implementation Example
When the Day 5 Resume Parser runs in production, it will wrap the candidate's data inside this metadata shell before saving it to the database:

```json
{
  "_metadata": {
    "candidate_id": "cnd_8f72a9b",
    "job_id": "job_3391xpf",
    "timestamp": "2026-02-23T14:30:00Z",
    "model_version": "resume_parser_v1.0",
    "document_status": "parsed"
  },
  "candidate_data": {
    "name": "Murthaja",
    "skills": ["Python", "Angular"]
  }
}