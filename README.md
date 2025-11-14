## RATS Reference Architecture — Empirical Evaluation

This repository contains the source code and benchmarking scripts used to evaluate the RATS (Reference Architecture for Trading Systems).

Note: For flexibility and ease of use, each core component is provided in both **.py** (Python script) and **.ipynb** (Jupyter Notebook) formats, allowing you to run the prototype either via terminal or interactively in a notebook environment.

## Structure

**execution_core/**  
Core execution engine (FastAPI, port 8000) — includes `main_core.py` and notebook.

**intermediary/**  
Request routing layer (FastAPI, port 8001) — includes `intermediary.py` and notebook.

**baseline/**  
Monolithic baseline service (FastAPI, port 8002) — includes `baseline.py` and notebook.

**end_user/**  
Client script (`end-user.py`) for sending requests and measuring metrics (latency, throughput, success rate).

**load_test_30Number/**  
Scripts for 30-concurrent-request benchmark (Sections 5.2–5.3).

**locust/**  
Locust load-testing configuration (`locustfile.py`) for 200 concurrent users (Section 5.4).

**locust_results/**  
Raw output and screenshots of Locust test results.

## How to Run

1. Install dependencies:  
   `pip install fastapi uvicorn locust requests`

2. Start services (in separate terminals or notebooks):  
   `uvicorn execution_core.main_core:app --port 8000`  
   `uvicorn intermediary.intermediary:app --port 8001`  
   `uvicorn baseline.baseline:app --port 8002`

3. Run benchmarks:  
   - 30 requests: execute scripts in `end_user/`  
   - 200 users:  
     `locust -f locust/locustfile.py --headless -u 200 -r 10 --run-time 1m`

## Important Notes

This is a research prototype for architectural validation. AI components generate synthetic BUY/SELL signals. The higher latency in RATS is an intentional trade-off for modifiability and scalability, as discussed in the manuscript.
