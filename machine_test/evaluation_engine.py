# machine_test/evaluation_engine.py
import json
import os

class MachineTestEngine:
    def __init__(self):
        """Initializes the engine and dynamically loads the adaptive task schema."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        schema_path = os.path.join(base_dir, 'task_schema.json')
        
        with open(schema_path, 'r') as f:
            self.schema = json.load(f)["task_types"]

    def _calculate_continuous_score(self, actual: float, optimal: float, absolute_max: float) -> float:
        """
        Replaces rigid step-functions with a smooth mathematical decay curve.
        If actual is better than optimal, score is 1.0.
        If actual crosses the max threshold, it decays smoothly down to a 0.1 floor score.
        """
        if actual <= optimal:
            return 1.0
        if actual >= absolute_max:
            return 0.1  # Minimum floor score instead of 0 to acknowledge effort
        
        # Smooth linear decay
        return 1.0 - ((actual - optimal) / (absolute_max - optimal) * 0.9)

    def assess_code_quality(self, code_string: str, max_lines: int) -> float:
        """Evaluates structural integrity rather than blindly counting lines."""
        lines = code_string.strip().split('\n')
        line_count = len(lines)
        
        # 1. Bloat penalty (using our continuous math)
        length_score = self._calculate_continuous_score(line_count, max_lines * 0.5, max_lines)
        
        # 2. Structural/Defensive Check (Does it use functions, classes, or try/except?)
        has_structure = 1.0 if any(kw in code_string for kw in ['def ', 'class ', 'try:']) else 0.5
        
        # 70% weight on being concise, 30% weight on using proper architecture
        return (length_score * 0.7) + (has_structure * 0.3)

    def evaluate_submission(self, task_type: str, execution_data: dict, candidate_code: str) -> dict:
        """The master grading pipeline that evaluates the candidate's output."""
        if task_type not in self.schema:
            raise ValueError(f"System Error: Unknown task type '{task_type}'")

        rules = self.schema[task_type]
        thresholds = rules["thresholds"]
        weights = rules["weights"]

        # 1. Correctness (Test Cases)
        passed = execution_data.get("passed", 0)
        total = execution_data.get("total", 1)
        correctness_score = passed / total

        # 2. Efficiency (Runtime Execution)
        runtime = execution_data.get("runtime_seconds", 999)
        efficiency_score = self._calculate_continuous_score(
            runtime, 
            thresholds["max_runtime_seconds"] * 0.3, # 30% of max limit is considered "optimal"
            thresholds["max_runtime_seconds"]
        )

        # 3. Code Quality (Structural Analysis)
        quality_score = self.assess_code_quality(candidate_code, thresholds["optimal_lines_max"])

        # 4. Problem Solving (Attempts / Compilation Errors)
        attempts = execution_data.get("attempts", 1)
        problem_solving_score = self._calculate_continuous_score(attempts, 1, thresholds["max_attempts"])

        # 5. Base Task Aggregation (Applying dynamic weights from JSON)
        task_score = (
            (correctness_score * weights["correctness"]) +
            (efficiency_score * weights["efficiency"]) +
            (quality_score * weights["code_quality"]) +
            (problem_solving_score * weights["problem_solving"])
        )

        # 6. Time Management Evaluation (80/20 final split)
        time_taken = execution_data.get("time_taken_minutes", thresholds["expected_time_minutes"])
        time_score = self._calculate_continuous_score(
            time_taken, 
            thresholds["expected_time_minutes"] * 0.5, 
            thresholds["expected_time_minutes"] * 1.5 # Allow going 50% over time with penalty
        )

        final_practical_score = (task_score * 0.8) + (time_score * 0.2)

        return {
            "task_score": round(final_practical_score * 100, 2),
            "sub_metrics": {
                "correctness": round(correctness_score * 100, 2),
                "efficiency": round(efficiency_score * 100, 2),
                "code_quality": round(quality_score * 100, 2),
                "time_management": round(time_score * 100, 2)
            },
            "applied_schema": task_type
        }