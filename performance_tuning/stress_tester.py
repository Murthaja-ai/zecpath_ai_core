# performance_tuning/stress_tester.py
import asyncio
import time
from optimized_engine import HighPerformanceEngine

def generate_mock_traffic(count: int) -> list:
    return [{"id": f"C_{i}", "scores": [90, 85, 88]} for i in range(count)]

async def run_benchmark():
    engine = HighPerformanceEngine()
    traffic = generate_mock_traffic(100) # 100 candidates applying at once
    
    print("\n📊 ZECPATH PERFORMANCE BENCHMARK REPORT")
    print("="*40)
    
    # --- TEST 1: The Old Way (Synchronous/Blocking) ---
    print("Testing Legacy Synchronous Pipeline...")
    start_sync = time.time()
    for payload in traffic:
        # Forcing it to wait one by one
        await engine._async_process_candidate(payload['id'], tuple(payload['scores']))
    sync_time = time.time() - start_sync
    print(f"Legacy Processing Time (100 reqs): {sync_time:.2f} seconds")

    # --- TEST 2: The New Way (Asynchronous Batching) ---
    print("\nTesting V2.0 Concurrent Batch Pipeline...")
    start_async = time.time()
    # Fires all 100 requests instantly
    await engine.batch_process(traffic)
    async_time = time.time() - start_async
    print(f"Optimized Processing Time (100 reqs): {async_time:.2f} seconds")
    
    print("="*40)
    improvement = ((sync_time - async_time) / sync_time) * 100
    print(f"🚀 Speed Improvement: {improvement:.1f}%\n")

if __name__ == "__main__":
    asyncio.run(run_benchmark())