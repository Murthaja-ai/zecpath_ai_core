from pydantic import BaseModel, Field

class ConfidenceSignals(BaseModel):
    hesitation: float
    length_score: float
    pace_score: float

class ConfidenceReport(BaseModel):
    confidence_score: float
    signals: ConfidenceSignals

class SentimentReport(BaseModel):
    sentiment: str = Field(..., description="'Positive', 'Neutral', or 'Negative'")
    sentiment_score: float

class BehaviorFlags(BaseModel):
    uncertainty: bool
    contradiction: bool

class BehavioralIndicators(BaseModel):
    """The final exact JSON structure requested by the company."""
    confidence: ConfidenceReport
    sentiment: SentimentReport
    behavior_flags: BehaviorFlags
    communication_strength: str = Field(..., description="'Strong', 'Moderate', or 'Weak'")