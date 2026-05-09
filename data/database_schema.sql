-- Master Table: Stores the overall interview session metadata
CREATE TABLE transcripts (
    transcript_id VARCHAR(50) PRIMARY KEY,
    candidate_id VARCHAR(50),
    job_id VARCHAR(50),
    language VARCHAR(10),
    overall_confidence FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Details Table: Stores the turn-by-turn conversation (The Tennis Match)
CREATE TABLE transcript_entries (
    entry_id SERIAL PRIMARY KEY,
    transcript_id VARCHAR(50) REFERENCES transcripts(transcript_id),
    question_id VARCHAR(50),
    question_text TEXT,
    answer_text TEXT,
    confidence_score FLOAT,
    start_time VARCHAR(10),
    end_time VARCHAR(10),
    duration_seconds INT
);