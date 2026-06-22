# performance_tuning/optimized_engine.py
import asyncio
import time
from functools import lru_cache
import statistics

class HighPerformanceEngine:
    def __init__(self):
        # We simulate a heavy standard deviation calculation
        pass

    @lru_cache(maxsize=5000)
    def cached_variance_penalty(self, score_tuple: tuple) -> float:
        """
        The Cache: If the system sees the exact same scores again, 
        it pulls the answer from memory instead of recalculating the math.
        (Note: lists cannot be cached, so we require a tuple).
        """
        if not score_tuple: return 0.0
        # Simulating heavy mathematical load
        time.sleep(0.01) # Simulated CPU cycle
        
        avg = sum(score_tuple) / len(score_tuple)
        if len(score_tuple) < 2: return avg
        
        variance = statistics.stdev(score_tuple)
        penalty = variance * 0.2
        return round(max(0.0, avg - penalty), 2)

    async def _async_process_candidate(self, candidate_id: str, scores: tuple) -> dict:
        """Simulates processing a single candidate asynchronously."""
        # Non-blocking wait simulates database lookup
        await asyncio.sleep(0.05) 
        final_score = self.cached_variance_penalty(scores)
        
        decision = "Selected" if final_score >= 80 else "Rejected"
        return {"id": candidate_id, "score": final_score, "decision": decision}

    async def batch_process(self, candidate_payloads: list) -> list:
        """
        The Concurrency Core: Processes an entire list of candidates simultaneously.
        """
        tasks = []
        for payload in candidate_payloads:
            scores_tuple = tuple(payload['scores'])
            task = asyncio.create_task(
                self._async_process_candidate(payload['id'], scores_tuple)
            )
            tasks.append(task)
            
        # Execute all 100 tasks at the exact same time
        results = await asyncio.gather(*tasks)
        return results

if __name__ == "__main__":
    print("\n🚀 TESTING CACHE EFFICIENCY")
    engine = HighPerformanceEngine()
    
    start = time.time()
    # First run: Does the heavy math
    res1 = engine.cached_variance_penalty((90, 80, 70))
    # Second run: Instantly pulled from memory
    res2 = engine.cached_variance_penalty((90, 80, 70))
    print(f"Time taken with Cache: {time.time() - start:.4f} seconds")