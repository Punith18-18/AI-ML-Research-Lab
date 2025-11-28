# Preth AI

Preth AI — minimal scaffolded project created by assistant for demonstration.

Overview
--------
A small demonstration FastAPI application that exposes a simple AI-like text completion endpoint. This scaffold includes:

- FastAPI backend
- Pydantic models
- A small, deterministic "completion" function (local, no external API calls)
- Unit tests using pytest
- `requirements.txt` for dependencies

Tech stack
----------
- Python 3.11+
- FastAPI
- Uvicorn (ASGI server)
- pytest for tests

How to run locally
------------------
1. Create a virtual environment (recommended):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run the server:

```powershell
uvicorn src.main:app --reload --port 8000
```

3. Open http://127.0.0.1:8000/docs for automated API docs (Swagger UI).

Key features
------------
- `/health` — health check
- `/complete` — simple deterministic text continuation endpoint

License
-------
MIT
