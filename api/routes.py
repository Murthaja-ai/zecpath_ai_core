from flask import Flask, request, jsonify
import sys
import os

# Ensure the app can find your screening_ai folder
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

from screening_ai.report_generator import generate_screening_report

app = Flask(__name__)

@app.route("/screening/start", methods=["POST"])
def start_screening():
    # 1. Receive JSON from the Frontend
    data = request.json
    
    candidate_id = data.get("candidate_id", "Unknown")
    job_id = data.get("job_id", "Unknown")
    answers = data.get("answers", [])
    scores = data.get("scores", [])
    behavior_reports = data.get("behavior", [])
    
    # 2. Process through your Day 28 Engine
    report = generate_screening_report(
        candidate_id=candidate_id,
        job_id=job_id,
        answers=answers,
        scores=scores,
        behavior_reports=behavior_reports
    )
    
    # 3. Send the final JSON back to the Frontend
    return jsonify(report)

if __name__ == "__main__":
    print("🚀 Zecpath AI API Server running on port 5000...")
    app.run(debug=True, port=5000)