# 🚀 Zecpath ATS - API Specification v1.0
**Architecture:** RESTful API with Asynchronous Job Polling

---

## 1. Resume Upload & Parsing (Async Flow)
Because AI extraction and semantic matching are computationally heavy, the parsing flow utilizes an asynchronous "Job ID" pattern to prevent browser timeouts.

### A. Initiate Parse Job
Uploads a candidate's resume and places it in the AI processing queue.

* **Endpoint:** `POST /api/v1/resumes/upload`
* **Content-Type:** `multipart/form-data`
* **Payload:**
  * `file`: The resume document (.pdf, .docx, .txt)

* **Success Response (202 Accepted):**
```json
{
  "status": "success",
  "message": "Resume uploaded and queued for processing.",
  "job_id": "job_8f72a9b1",
  "check_status_url": "/api/v1/jobs/job_8f72a9b1"
}
```

---

### B. Check Job Status (Polling)
The frontend uses this endpoint every 3-5 seconds to check the status of the AI pipeline.

* **Endpoint:** `GET /api/v1/jobs/{job_id}`
* **Content-Type:** `application/json`

* **Response: Processing (200 OK):**
```json
{
  "job_id": "job_8f72a9b1",
  "status": "processing",
  "progress_percent": 45,
  "current_step": "Extracting Semantic Skills..."
}
```

* **Response: Completed (200 OK):**
```json
{
  "job_id": "job_8f72a9b1",
  "status": "completed",
  "result": {
      "candidate_id": "Candidate_93B2",
      "total_experience_years": 4.5,
      "extracted_skills": ["Python", "React", "AWS"]
  }
}
```

---

## 2. Scoring & Shortlisting (Synchronous Flow)
Because the heavy AI parsing is already done, the math to compare a Job Description against parsed resumes is lightning fast. This endpoint operates synchronously.

### A. Generate HR Shortlist
Takes a Job Description and a list of parsed candidates, applies the JSON business rules, curves the grades, and returns the final HR Dashboard data.

* **Endpoint:** `POST /api/v1/ats/score`
* **Content-Type:** `application/json`

* **Request Payload:**
```json
{
  "job_description": {
    "job_title": "Software Engineer",
    "required_skills": ["Python", "AWS", "React"],
    "minimum_experience_years": 3
  },
  "candidates": [
    {
      "candidate_id": "Candidate_93B2",
      "total_experience_years": 4.5,
      "extracted_skills": ["Python", "React", "AWS"]
    }
  ]
}
```

* **Success Response (200 OK):**
```json
{
  "status": "success",
  "total_processed": 1,
  "shortlisted_candidates": [
    {
      "candidate_id": "Candidate_93B2",
      "curved_score": 100.0,
      "ats_status": "Shortlisted",
      "recruiter_note": "Shortlisted due to 100.0% curved match. (Skills: 100%, Exp: 100%)"
    }
  ],
  "review_candidates": [],
  "rejected_candidates": []
}
```

* **Error Response (400 Bad Request):**
```json
{
  "error_code": "MISSING_JD_DATA",
  "message": "The job_description payload must include 'job_title' and 'required_skills'."
}
```
---

## 3. Integration Flow (The Frontend/Backend Sequence)
To build a successful UI/UX, the frontend system should follow this exact sequence:

1. **Upload Phase:** User drops 50 resumes into the UI. Frontend calls `POST /api/v1/resumes/upload` 50 times.
2. **Waiting Phase:** Frontend receives 50 `job_id`s. UI displays a progress bar.
3. **Polling Phase:** Frontend calls `GET /api/v1/jobs/{job_id}` every 5 seconds. As each job returns `"status": "completed"`, the progress bar fills up.
4. **Scoring Phase:** Once all 50 resumes are parsed, Frontend bundles the 50 JSON results and the Job Description, and sends them to `POST /api/v1/ats/score`.
5. **Display Phase:** The API instantly returns the curated, curved, and anonymized shortlist. The Frontend renders the final HR Dashboard.

---

## 4. Error & Logging Standards

### A. API Error Contract
All API errors will strictly follow this JSON schema to ensure the frontend can gracefully handle failures:
```json
{
  "error_code": "STRING_ENUM",
  "message": "Human-readable explanation of what went wrong."
}

### B. Standard HTTP Status Codes
* **200 OK:** Synchronous success.
* **202 Accepted:** Asynchronous task started.
* **400 Bad Request:** Missing fields in the JSON payload.
* **404 Not Found:** `job_id` does not exist.
* **415 Unsupported Media Type:** File uploaded is not a PDF/DOCX.
* **500 Internal Server Error:** AI engine failure (Timeout, Out of Memory).

### C. Backend Logging Standards
For the DevOps and Backend team, all microservices must log:
1. **Trace IDs:** Every request must generate a unique UUID trace ID.
2. **Async Failures:** If `sentence-transformers` fails, the stack trace must be logged to a central server (e.g., Datadog, AWS CloudWatch) tagging the `job_id`.
3. **Audit Trails:** For EEOC/Fairness compliance, any penalty applied to a score (e.g., Anti-Cheat penalty) must be logged permanently in the backend database.

### D. Rate Limiting & Security
Because AI inference (parsing/scoring) is computationally expensive, the API enforces strict rate limiting to prevent DDoS attacks and resource exhaustion.
* **Uploads (`POST /resumes/upload`):** Max 50 requests per minute per IP address.
* **Polling (`GET /jobs/{job_id}`):** Max 100 requests per minute per IP address.
* **Headers:** All responses will include standard rate limit headers:
  * `X-RateLimit-Limit`
  * `X-RateLimit-Remaining`
  * `X-RateLimit-Reset`