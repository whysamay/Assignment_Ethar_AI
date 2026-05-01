# Day Planner

**Live App:** [https://web-production-28696.up.railway.app](https://web-production-28696.up.railway.app)

Day Planner is a streamlined tool designed to help individuals and teams organize their workload. Instead of dealing with bloated software, this app keeps things simple: you can create projects, break them down into actionable tasks, and track overall progress through a clean, aggregated dashboard.

It includes built-in Role-Based Access Control (RBAC), meaning you can have Admins who manage the overall system and standard Users who interact with their assigned work. It's built to be fast, responsive, and easy to deploy.

## Stack
- **Backend:** FastAPI, Python, SQLAlchemy, SQLite
- **Frontend:** Vanilla HTML, CSS, JavaScript

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Mac/Linux
source .venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Start the dev server:
```bash
uvicorn main:app --reload
```

The app will be available at `http://localhost:8000`. 
API docs are auto-generated at `http://localhost:8000/docs`.

## Running Tests
Tests are written with `pytest`.
```bash
pytest Testing/
```
