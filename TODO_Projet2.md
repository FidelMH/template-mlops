# TODO - Projet 2 : Orchestration, Sécurité et Livraison Continue

## 1. API FastAPI (`app_api/`)

### `app_api/main.py`
- [x] Créer l'application FastAPI
- [ ] Configurer CORS
- [x] Inclure les routes (CRUD)
- [x] Ajouter l'endpoint de santé (`GET /`)

### `app_api/models/models.py`
- [x] Définir le modèle SQLAlchemy (table principale du projet)
- [ ] Configurer la base de données (Base, engine, SessionLocal)

### `app_api/modules/connect.py`
- [ ] Configurer la connexion à la base de données via variables d'environnement
- [ ] Exposer `get_db` (dépendance FastAPI)

### `app_api/modules/crud.py`
- [ ] Implémenter `create_item`
- [ ] Implémenter `read_items`
- [ ] Implémenter `read_item` (par id)
- [ ] Implémenter `update_item`
- [ ] Implémenter `delete_item`

### `app_api/pyproject.toml`
- [ ] Ajouter `uvicorn` aux dépendances
- [ ] Ajouter `httpx` aux dépendances (pour les tests)
- [ ] Décommenter / corriger la section `[tool.pytest.ini_options]`

---

## 2. Frontend Streamlit (`app_front/`)

### `app_front/main.py`
- [ ] Réécrire en Streamlit (page d'accueil / navigation)
- [ ] Supprimer l'ancien code non-Streamlit

### `app_front/pages/0_insert.py`
- [ ] Formulaire Streamlit pour créer un enregistrement (appel `POST` à l'API)

### `app_front/pages/1_read.py`
- [ ] Tableau Streamlit pour lister les enregistrements (appel `GET` à l'API)

### `app_front/pyproject.toml`
- [ ] Ajouter `requests` aux dépendances

---

## 3. Docker

### `app_api/Dockerfile`
- [ ] Image Python avec `uv`
- [ ] Copier `pyproject.toml` et installer les dépendances
- [ ] Copier le code source
- [ ] Exposer le port et lancer `uvicorn`

### `app_front/Dockerfile`
- [ ] Image Python avec `uv`
- [ ] Copier `pyproject.toml` et installer les dépendances
- [ ] Copier le code source
- [ ] Exposer le port et lancer `streamlit run`

### `docker-compose.yml` (développement)
- [ ] Service `api` (build `app_api/`, port 8000)
- [ ] Service `front` (build `app_front/`, port 8501, dépend de `api`)
- [ ] Service `db` (PostgreSQL, variables d'env depuis `.env`)
- [ ] Volume persistant pour la base de données

### `docker-compose.prod.yml` (production)
- [ ] Utiliser les images DockerHub au lieu de `build:`
- [ ] Surcharger les variables d'environnement de production

### `.env.example`
- [ ] Lister toutes les variables d'environnement nécessaires (`DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `API_URL`, etc.)

### `.dockerignore`
- [ ] Exclure `__pycache__`, `*.pyc`, `.env`, `.venv`, `*.egg-info`, `.pytest_cache`, `htmlcov/`

---

## 4. Tests

### `conftest.py`
- [ ] Configurer le client de test FastAPI (`TestClient`)
- [ ] Configurer une base de données de test (SQLite en mémoire ou fixture PostgreSQL)
- [ ] Exposer les fixtures partagées

### `tests/test_api.py`
- [ ] Test `POST /items` (création)
- [ ] Test `GET /items` (lecture liste)
- [ ] Test `GET /items/{id}` (lecture unitaire)
- [ ] Test `PUT /items/{id}` (mise à jour)
- [ ] Test `DELETE /items/{id}` (suppression)

---

## 5. CI/CD GitHub Actions

### `.github/workflows/ci.yml` (corrections)
- [ ] Corriger le chemin pytest : `uv run pytest --cov=app_api tests/`
- [ ] Ajouter l'étape Gitleaks (scan de secrets) ou déléguer à `security.yml`

### `.github/workflows/security.yml` (à créer)
- [ ] Déclencher sur `push` et `pull_request`
- [ ] Utiliser l'action `gitleaks/gitleaks-action` pour scanner les secrets

### `.github/workflows/cd.yml` (à créer)
- [ ] Déclencher sur `push` sur `main` (après CI réussie)
- [ ] Se connecter à DockerHub (`DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN` en secrets)
- [ ] Builder et pousser l'image `app_api`
- [ ] Builder et pousser l'image `app_front`
- [ ] Tagger avec le SHA du commit et `latest`

---

## 6. Sécurité et bonnes pratiques

### `.gitignore`
- [ ] Ajouter `.env` (actuellement absent)

### `.github/CONTRIBUTING.md` (à créer)
- [ ] Décrire le workflow de contribution (branches, PRs, conventions de commit)
- [ ] Documenter comment lancer le projet en local (Docker Compose)
- [ ] Documenter comment lancer les tests

---

## Récapitulatif des fichiers à créer / modifier

| Fichier | Action |
|---|---|
| `app_api/main.py` | A remplir |
| `app_api/models/models.py` | A remplir |
| `app_api/modules/connect.py` | A remplir |
| `app_api/modules/crud.py` | A remplir |
| `app_api/pyproject.toml` | A corriger |
| `app_api/Dockerfile` | A remplir |
| `app_front/main.py` | A réécrire |
| `app_front/pages/0_insert.py` | A remplir |
| `app_front/pages/1_read.py` | A remplir |
| `app_front/pyproject.toml` | A corriger |
| `app_front/Dockerfile` | A remplir |
| `docker-compose.yml` | A remplir |
| `docker-compose.prod.yml` | A remplir |
| `.env.example` | A remplir |
| `.dockerignore` | A remplir |
| `conftest.py` | A remplir |
| `tests/test_api.py` | A remplir |
| `.gitignore` | A corriger (ajouter `.env`) |
| `.github/workflows/ci.yml` | A corriger (chemin pytest) |
| `.github/workflows/security.yml` | A créer |
| `.github/workflows/cd.yml` | A créer |
| `.github/CONTRIBUTING.md` | A créer |
