from pydantic import BaseModel, Field
from typing import List

class SubScores(BaseModel):
    clarity: float
    relevance: float
    completeness: float
    consistency: float

class Explanations(BaseModel):
    clarity: str
    relevance: str
    completeness: str
    consistency: str

class QuestionScore(BaseModel):
    """The granular report card for a single interview answer."""
    question_id: str
    scores: SubScores
    final_score: float = Field(..., description="Score out of 100")
    explanation: Explanations

class SummaryAverages(BaseModel):
    avg_clarity: float
    avg_relevance: float
    avg_completeness: float
    avg_consistency: float

class FinalScreeningScore(BaseModel):
    """The ultimate evaluation object that dictates the candidate's fate."""
    candidate_id: str
    screening_score: float = Field(..., description="Overall score out of 100")
    decision: str = Field(..., description="'Pass', 'Review', or 'Reject'")
    breakdown: List[QuestionScore]
    summary: SummaryAverages