# Zecpath AI Core: Master API Integration Contract (V1.0)

## 1. Architectural Rules
* **The Envelope Rule:** Every single response from the AI API, regardless of endpoint, will return a strict JSON envelope containing `status`, `data`, and `error_details`.
* **The Consent Rule:** Every evaluation request MUST include a `legal_consent_granted: boolean` flag, or the API will return a `403 Forbidden` error.

---

## 2. Endpoint 1: The Async Resume Parser
**URL:** `POST /api/v1/ai/parse-resume`
**Pattern:** Asynchronous (Webhook/Polling)
**Purpose:** Processing a 10-page PDF takes heavy compute. We do not freeze the frontend. We accept the file and return a `job_id` instantly.

**Request (From React to AI):**
```json
{
  "candidate_id": "C_105",
  "legal_consent_granted": true,
  "file_url": "https://s3.aws.com/zecpath/resumes/c_105.pdf"
}
```

**Immediate Response (Sync):**
```json
{
  "status": "PROCESSING",
  "data": { "job_id": "job_99823", "estimated_time_sec": 12 },
  "error_details": null
}
```

---

## 3. Endpoint 2: The Sync Live Interview Scorer
**URL:** `POST /api/v1/ai/score-interview`
**Pattern:** Synchronous (Real-time)
**Purpose:** The candidate just answered a question. We need an instant score to determine the next question.

**Request:**
```json
{
  "candidate_id": "C_105",
  "session_id": "S_444",
  "transcript": "I optimized the React rendering cycle by using useMemo.",
  "legal_consent_granted": true
}
```

**Response (Instant):**
```json
{
  "status": "SUCCESS",
  "data": { "technical_score": 92.5, "flagged_for_review": false },
  "error_details": null
}
```

---

## 4. Endpoint 3: Final End-to-End Decision
**URL:** `POST /api/v1/ai/generate-decision`
**Pattern:** Synchronous
**Purpose:** Triggers the Day 54 Variance Engine and the Day 56 Pipeline.

**Request:**
```json
{
  "candidate_id": "C_105",
  "legal_consent_granted": true,
  "scores": { "ats": 85.0, "hr": 90.0, "technical": 92.5 }
}
```

**Response:**
```json
{
  "status": "SUCCESS",
  "data": {
    "candidate_id": "C_105",
    "final_score": 89.1,
    "decision": "Selected"
  },
  "error_details": null
}
```