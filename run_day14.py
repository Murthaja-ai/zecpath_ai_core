from utils.ranking_engine import RankingEngine

def run_shortlisting_simulation():
    # 1. Initialize our new Ranking Factory
    ranker = RankingEngine()
    
    # 2. Create 5 Mock Candidates
    # Notice that Alice and Bob both got exactly 82.5%. 
    # But Alice has higher raw skills (0.90 vs 0.85). The Tie-Breaker should catch this!
    mock_candidates = [
        {"candidate_name": "David (The Intern)", "final_score": 0.450, "raw_scores": {"skills": 0.40, "experience": 0.10}},
        {"candidate_name": "Alice (The Expert)", "final_score": 0.825, "raw_scores": {"skills": 0.90, "experience": 0.80}},
        {"candidate_name": "Eve (The Solid Mid)", "final_score": 0.760, "raw_scores": {"skills": 0.80, "experience": 0.70}},
        {"candidate_name": "Charlie (The Junior)", "final_score": 0.600, "raw_scores": {"skills": 0.65, "experience": 0.30}},
        {"candidate_name": "Bob (The Generalist)", "final_score": 0.825, "raw_scores": {"skills": 0.85, "experience": 0.85}}
    ]
    
    # 3. Push the candidates through the engine
    print("\n⚙️ Processing 5 candidates through the Shortlisting Factory...\n")
    final_report = ranker.rank_and_filter(mock_candidates)
    
    # 4. Print the Recruiter-Friendly Dashboard
    print("="*80)
    print("📊 HR DASHBOARD: AUTOMATED CANDIDATE SHORTLIST")
    print("="*80)
    print(f"{'RANK':<5} | {'CANDIDATE NAME':<22} | {'SCORE':<6} | {'STATUS':<15} | {'RECOMMENDED ACTION'}")
    print("-" * 80)
    
    for index, candidate in enumerate(final_report):
        rank = index + 1
        name = candidate["candidate_name"]
        score = f"{candidate['final_percentage']}%"
        status = candidate["ats_status"]
        action = candidate["ats_action"]
        
        # Add some visual emojis based on status
        if status == "Shortlisted":
            status = f"🟢 {status}"
        elif status == "Needs Review":
            status = f"🟡 {status}"
        else:
            status = f"🔴 {status}"
            
        print(f" #{rank:<3} | {name:<22} | {score:<6} | {status:<15} | {action}")
        
    print("="*80)
    # 5. Export to CSV for the Recruiter
    ranker.export_to_csv(final_report)

if __name__ == "__main__":
    run_shortlisting_simulation()