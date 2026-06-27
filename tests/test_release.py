from core.release_ready_system import release_pipeline

def test_release_standard_flow():
    result = release_pipeline("C100", {"ats": 90, "hr": 85, "tech": 92})
    assert result["decision"] == "SELECTED"
    assert result["final_score"] > 80

def test_release_edge_cases():
    # Tests that the system safely clamps 150 to 100, and -50 to 0
    result = release_pipeline("C101", {"ats": 150, "hr": -50})
    assert result["final_score"] <= 100
    assert result["final_score"] >= 0
    assert result["status"] == "RELEASE_READY"

def test_release_hard_gate():
    # Tests that a cheater with perfect scores gets an automatic zero
    result = release_pipeline("C102", {"ats": 99, "tech": 99}, integrity_flags=1)
    assert result["decision"] == "REJECTED (Integrity Violation)"
    assert result["final_score"] == 0.0