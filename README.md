Clinical Workflow Automation Agent

This project implements a function-calling LLM agent that orchestrates clinical workflows by interacting with deterministic healthcare APIs.

The agent interprets natural language requests, selects validated tools, executes API calls, and returns structured outputs with full audit logging.

No medical advice or diagnosis is generated.

Run FastAPI:
uvicorn api.main:app --reload

Run agent:
python run_agent.py
