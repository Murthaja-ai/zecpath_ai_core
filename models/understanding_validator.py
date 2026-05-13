from pydantic import BaseModel, Field
from typing import List, Optional
from screening_ai.intent_classifier import AnswerIntent

class UnderstoodAnswer(BaseModel):
    """
    The strict schema matching the company's flat JSON requirements.
    """
    question_id: str
    original_text: str
    intent: AnswerIntent
    skills: List[str] = Field(default_factory=list)
    experience_years: Optional[int] = 0
    salary: Optional[str] = None
    availability: str = "Unknown"
    
    # Quality Check Flags
    off_topic: bool
    is_vague: bool
    is_missing: bool