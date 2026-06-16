# optimization_core/test_optimization.py
from score_refiner import StatisticalScoreRefiner
from engine_tuner import OptimizedDecisionEngine
from batch_processor import ConcurrentBatchProcessor

def run_optimization_suite():
    print("🚀 Initializing Day 54 Algorithmic Optimization Suite...\n")

    # Target 1: Verify Statistical Consistency Tuning
    volatile_scores = {"ats": 95.0, "technical": 90.0, "hr": 40.0}
    adjustment = StatisticalScoreRefiner.calculate_consistency_adjustment(volatile_scores)
    print(f"✔ [Metric Test] Volatile Profile Variance Penalty: {adjustment} pts")
    assert adjustment < 0, "Failed to penalize high score volatility."

    # Target 2: Verify Hard-Gate Override Interception
    engine = OptimizedDecisionEngine()
    decision = engine.evaluate_candidate_edge_cases(refined_score=85.0, technical_score=90.0, integrity_status="High Risk")
    print(f"✔ [Gate Test] High Score + High Integrity Risk Outcome: {decision}")
    assert decision == "Rejected", "Security failure: Hard gate did not intercept integrity risk."

    # Target 3: Test Concurrent Thread-Pool Scalability
    mock_batch = [
        {"refined_score": 82.0, "technical_score": 88.0, "integrity": "Low Risk"},
        {"refined_score": 52.0, "technical_score": 87.0, "integrity": "Low Risk"},
        {"refined_score": 89.0, "technical_score": 92.0, "integrity": "High Risk"}
    ]

    def process_node(item):
        return engine.evaluate_candidate_edge_cases(item["refined_score"], item["technical_score"], item["integrity"])

    batch_outcomes = ConcurrentBatchProcessor.execute_parallel_pipeline(mock_batch, process_node)
    print(f"✔ [Batch Test] Concurrent Processing Strategy Outcomes executed successfully.")
    print(f"  -> Processed {len(batch_outcomes)} candidate profiles concurrently.")
    
    print("\n🎉 All Day 54 Optimization Checkpoints Passed Successfully.")

if __name__ == "__main__":
    run_optimization_suite()