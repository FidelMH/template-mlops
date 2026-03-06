# python-professional-template

A DevOps training project: 3-tier microservices app with CI/CD, code quality, and automated documentation.

[![CI](https://github.com/FidelMH/template-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/FidelMH/template-mlops/actions)
![Coverage](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFidelMH%2F1392a599fe97be53ef0d5cff77225b7e%2Fraw%2F5cae9e33426c2a2bf734c9d9679f9dcdc1276f46%2Fcoverage.json)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Stack

- **Backend:** Python 3.11, FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** Streamlit
- **Quality:** ruff (lint + format), pytest + coverage
- **Docs:** Sphinx → GitHub Pages
- **CI/CD:** GitHub Actions, Docker Hub

## Architecture

```
Streamlit (8501) → FastAPI (8000) → PostgreSQL (5432)
```

| Service    | Role                              | Port |
|------------|-----------------------------------|------|
| `app_front` | Streamlit UI (list/add users)    | 8501 |
| `app_api`   | REST API (CRUD users)            | 8000 |
| `db`        | PostgreSQL database              | 5432 |

## Requirements

- Docker & Docker Compose

## Quick Start

```bash
cp .env.example .env
docker-compose up --build
```

- Frontend: http://localhost:8501
- API docs: http://localhost:8000/docs

## Environment Variables

See [.env.example](.env.example) for all variables.

| Variable            | Description               | Default (local)          |
|---------------------|---------------------------|--------------------------|
| `DATABASE_URL`      | Database connection string | `sqlite:///./local.db`  |
| `POSTGRES_USER`     | PostgreSQL username        | —                       |
| `POSTGRES_PASSWORD` | PostgreSQL password        | —                       |
| `POSTGRES_DB`       | Database name              | —                       |

## API Endpoints

| Method | Route     | Description        |
|--------|-----------|--------------------|
| GET    | `/health` | Health check       |
| GET    | `/data`   | List all users     |
| POST   | `/data`   | Create a new user  |

**POST /data body:**
```json
{ "name": "Alice", "age": 30, "score": 95.5 }
```

## Development Commands

```bash
make check     # lint + format check
make fix-lint  # auto-fix lint issues
make test      # run tests with coverage
```

To run locally without Docker (inside `app_api/` or `app_front/`):
```bash
uv sync
uv run python main.py
```

## CI/CD Pipelines

| Workflow        | Trigger           | Action                                     |
|-----------------|-------------------|--------------------------------------------|
| `ci.yml`        | push / PR         | Lint (ruff) + tests + coverage badge       |
| `cd.yml`        | push to `main`    | Build & push Docker images to Docker Hub   |
| `docs.yml`      | push to `main`    | Build Sphinx docs → GitHub Pages           |
| `security.yml`  | push / PR / daily | Secret scanning with gitleaks              |

## Project Structure

```
.
├── app_api/           # FastAPI backend
│   ├── main.py
│   ├── maths/
│   ├── models/
│   └── modules/       # DB connection & CRUD
├── app_front/         # Streamlit frontend
│   ├── main.py
│   └── pages/
├── tests/
├── docs/source/
├── .github/workflows/
├── docker-compose.yml
├── Makefile
└── pyproject.toml
```

## Contributors

- [@FidelMH](https://github.com/FidelMH)
