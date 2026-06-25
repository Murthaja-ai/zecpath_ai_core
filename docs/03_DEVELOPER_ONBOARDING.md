# Welcome to Zecpath AI: Developer Onboarding

Welcome to the team! You are working on one of the most advanced, high-performance AI hiring engines in the world. Please read this guide carefully before submitting your first Pull Request.

## 1. The Golden Rules of Zecpath
1. **Never Block the Main Thread:** We process thousands of candidates a minute. Do not use standard `for` loops for batch processing. You **must** use `asyncio.gather()` to execute mathematical operations concurrently.
2. **Never Log Plain Text PII:** You are legally liable for data privacy. Never use `print(candidate_data)`. You must use the `ZecpathTelemetry.log_event()` class, which automatically masks emails and phone numbers.
3. **Never Break the Envelope:** All API endpoints must return exactly three keys: `status`, `data`, and `error_details`. If you return a random JSON structure, you will crash the React frontend.

## 2. Repository Structure
* `/parsers/` - Contains the Knowledge Graph and ATS PDF logic.
* `/api_integration/` - Contains the Gateway, JWT Middleware, and Async Webhooks.
* `/performance_tuning/` - Contains the LRU Caches and Auto-Scaling logic.
* `/observability_core/` - Contains the Telemetry Logger and Cryptographic Vault.

## 3. Quickstart: Running the System Locally
1. Activate your virtual environment: `source venv/bin/activate`
2. Ensure you have the test API keys in your `.env` file.
3. Run the telemetry test to ensure your local logs are masking PII: `python observability_core/telemetry_logger.py`
4. Run the high-performance stress test to verify CPU threading: `python performance_tuning/stress_tester.py`

*If the stress test shows a latency reduction of >95%, your environment is ready.*