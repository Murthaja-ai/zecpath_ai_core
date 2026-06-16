# optimization_core/batch_processor.py
import concurrent.futures
from typing import List, Callable, Any

class ConcurrentBatchProcessor:
    @staticmethod
    def execute_parallel_pipeline(data_batch: List[Any], processing_func: Callable[[Any], Any], max_workers: int = 4) -> List[Any]:
        """
        Executes pipeline processing concurrently across multiple background workers.
        Replaces slow sequential iterations with an optimized thread-pool infrastructure.
        """
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Map the processing function across all batch entries concurrently
            future_to_item = {executor.submit(processing_func, item): item for item in data_batch}
            
            for future in concurrent.futures.as_completed(future_to_item):
                try:
                    # Append the successfully processed candidate data
                    results.append(future.result())
                except Exception as exc:
                    # Log standard processing fault trace without crashing the entire batch
                    results.append({"status": "System Error", "exception": str(exc)})
                    
        return results