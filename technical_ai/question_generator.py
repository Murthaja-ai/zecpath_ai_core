# technical_ai/question_generator.py
import random

def fetch_next_question(role: str, current_difficulty: str, asked_questions: list) -> dict:
    """
    Pulls a secure, non-repeated question from the active domain hierarchy.
    """
    
    # Simulated database response based on our json hierarchy mapping
    MOCK_DATABASE = {
        "frontend_developer": {
            "basic": ["Explain the JavaScript Event Loop.", "What is the difference between let, const, and var?"],
            "intermediate": ["How do you manage state in a large Angular application?", "Explain CSS Grid vs Flexbox with a real-world scenario."],
            "advanced": ["Design a scalable Micro-Frontend architecture.", "How would you optimize Webpack for a massive enterprise UI?"]
        },
        "data_scientist": {
            "basic": ["What is a p-value?", "Explain the difference between a list and a tuple in Python."],
            "intermediate": ["How do you handle missing data in a Pandas DataFrame?", "Explain the bias-variance tradeoff."],
            "advanced": ["Design a real-time recommendation engine infrastructure.", "How do you deploy and scale a model in production?"]
        }
    }
    
    # Securely extract the domain questions
    domain_questions = MOCK_DATABASE.get(role, {}).get(current_difficulty, [])
    
    # Filter out questions that have already been asked to prevent looping
    available_questions = [q for q in domain_questions if q not in asked_questions]
    
    if not available_questions:
        return {"error": "Question bank exhausted for this tier.", "question": None}
        
    selected_question = random.choice(available_questions)
    
    return {
        "question": selected_question,
        "domain": role,
        "difficulty_pulled": current_difficulty
    }