import random
import json
import os

def load_question_bank():
    """Loads the HR question bank JSON file."""
    # Ensure we get the absolute path so it runs from anywhere
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "question_bank.json")
    
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_questions(role_type: str, experience_level: str) -> list:
    """
    Dynamically generates a tailored interview playlist based on candidate persona.
    role_type: 'technical' or 'non_technical'
    experience_level: 'fresher' or 'experienced'
    """
    qb = load_question_bank()
    questions = []
    
    # 1. Phase: Introduction (Tailored to experience)
    questions += qb["categories"]["introduction"].get(experience_level, [])
    
    # 2. Phase: Core HR Questions (Common to everyone)
    for cat in ["strengths_weaknesses", "teamwork", "career_goals"]:
        questions += qb["categories"][cat]["common"]
        
    # 3. Phase: Role-Based Evaluation (Tailored to tech/non-tech)
    questions += qb["role_based"].get(role_type, [])
    
    # 4. Phase: Closing (Availability)
    closing_questions = qb["categories"]["availability"]["common"]
    
    # Randomize the core questions to ensure no two interviews are identical
    # but keep the total length manageable (e.g., max 6 core questions)
    selected_core = random.sample(questions, min(5, len(questions)))
    
    # Ensure closing questions always happen at the end
    final_playlist = selected_core + [closing_questions[0]]
    
    return final_playlist

if __name__ == "__main__":
    # Quick Test
    print("🧪 Generating Test Interview for: Technical Fresher")
    playlist = generate_questions("technical", "fresher")
    for i, q in enumerate(playlist, 1):
        print(f"Q{i}: {q}")