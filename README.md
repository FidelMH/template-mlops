# python-professional-template

Exercice DevOps : template Python avec tests, qualité de code, documentation et CI/CD.

[![Build Status](https://github.com/FidelMH/template-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/FidelMH/template-mlops/actions)
![Coverage](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fgist.githubusercontent.com%2FFidelMH%2F1392a599fe97be53ef0d5cff77225b7e%2Fraw%2F5cae9e33426c2a2bf734c9d9679f9dcdc1276f46%2Fcoverage.json&query=%24.message)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Stack

- Python 3.11 · [uv](https://github.com/astral-sh/uv)
- Tests : pytest + coverage
- Qualité : ruff (lint + format)
- Docs : Sphinx → GitHub Pages
- CI/CD : GitHub Actions

## Installation

```bash
uv sync
```

## Commandes

```bash
uv run python app/main.py   # lancer l'app
uv run pytest               # tests + coverage
uv run ruff check .         # lint
uv run ruff format .        # format
```

## Docker

```bash
docker build -t python-professional-template .
docker run python-professional-template
```

## Code de conduite

Ce projet respecte le [Contributor Covenant](.github/CODE_OF_CONDUCT.md).

## Contributeurs

- [@FidelMH](https://github.com/FidelMH)

## Structure

```
.
├── app/
│   ├── main.py
│   ├── moncsv.csv
│   └── modules/mon_module.py
├── tests/
│   └── test_match_csv.py
├── docs/source/
├── .github/workflows/
│   ├── ci.yml     # lint + tests + badge coverage
│   └── docs.yml   # déploiement GitHub Pages
├── Dockerfile
└── pyproject.toml
```
