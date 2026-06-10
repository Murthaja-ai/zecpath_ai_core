# technical_ai/experience_logic.py

def calculate_initial_state(years_of_experience: float) -> dict:
    """
    Determines the candidate's starting difficulty tier based on resume experience.
    
    Args:
        years_of_experience (float): The total years of domain-specific experience.
        
    Returns:
        dict: The mapped experience band and the designated initial difficulty.
    """
    
    # Defensive programming: Prevent negative experience inputs
    if years_of_experience < 0:
        raise ValueError("Critical Error: Years of experience cannot be negative.")
        
    # Map to the 0-2 Years Band (Basic)
    if years_of_experience <= 2.5:
        return {
            "experience_band": "0-2", 
            "initial_difficulty": "basic"
        }
        
    # Map to the 3-5 Years Band (Intermediate)
    elif years_of_experience <= 5.0:
        return {
            "experience_band": "3-5", 
            "initial_difficulty": "intermediate"
        }
        
    # Map to the 5+ Years Band (Advanced)
    else:
        return {
            "experience_band": "5+", 
            "initial_difficulty": "advanced"
        }

# --- Quick Test Execution ---
if __name__ == "__main__":
    print("Testing Junior Developer (1.5 years):", calculate_initial_state(1.5))
    print("Testing Mid-Level Developer (4.0 years):", calculate_initial_state(4.0))
    print("Testing Senior Architect (8.5 years):", calculate_initial_state(8.5))