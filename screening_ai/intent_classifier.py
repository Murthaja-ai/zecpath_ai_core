from enum import Enum

class AnswerIntent(str, Enum):
    """
    Strict categorization of HR topics based on company requirements.
    """
    INTRODUCTION = "introduction"
    EXPERIENCE = "experience"
    SKILLS = "skills"
    SALARY = "salary"
    AVAILABILITY = "availability"
    UNKNOWN = "unknown"