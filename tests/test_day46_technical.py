# tests/test_day46_technical.py
from technical_ai.experience_logic import calculate_initial_state

def test_experience_routing():
    """Validates that candidate years are correctly routed to difficulty tiers."""
    
    # Test Junior
    assert calculate_initial_state(1.5)["initial_difficulty"] == "basic"
    assert calculate_initial_state(1.5)["experience_band"] == "0-2"
    
    # Test Mid-Level
    assert calculate_initial_state(3.5)["initial_difficulty"] == "intermediate"
    
    # Test Senior
    assert calculate_initial_state(7.0)["initial_difficulty"] == "advanced"