from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

# 1. Define the Metadata Rules
class TranscriptMetadata(BaseModel):
    candidate_id: str
    job_id: str
    interview_date: datetime
    language_detected: str = Field(default="en", max_length=2)
    overall_audio_quality: str

# 2. Define the Normalization Rules
class NormalizationRules(BaseModel):
    remove_filler_words: bool = True
    lowercase_conversion: bool = True
    punctuation_stripped: bool = True

# 3. Define the Dialogue Turn Rules (The Tennis Match)
class DialogueTurn(BaseModel):
    turn_id: int
    speaker: str = Field(..., description="Must be 'AI' or 'Candidate'")
    question_id: Optional[str] = None  
    raw_text: str
    normalized_text: Optional[str] = None
    confidence_level: Optional[float] = Field(None, ge=0.0, le=1.0) 
    timestamp: datetime
    duration_seconds: Optional[int] = None 
    flagged_for_review: bool = False

# 4. The Master Transcript Model
class TranscriptSession(BaseModel):
    session_id: str
    metadata: TranscriptMetadata
    normalization_rules_applied: NormalizationRules
    dialogue_turns: List[DialogueTurn]
    session_status: str = Field(default="in_progress")

# --- Quick Test Function ---
if __name__ == "__main__":
    print("🛡️ Booting up Transcript Validator...")
    print("✅ Pydantic models successfully compiled! The Enforcer is ready.")