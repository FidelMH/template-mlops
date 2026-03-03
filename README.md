# python-professional-template

A Python project template demonstrating professional development practices: modular code, testing, documentation, and code quality tooling.


[![Build Status](https://github.com/FidelMH/template-mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/FidelMH/template-mlops/actions)
![Coverage](https://img.shields.io/endpoint?url=https%3A%2F%2Fgist.githubusercontent.com%2FFidelMH%2F1392a599fe97be53ef0d5cff77225b7e%2Fraw%2F10987a85029f6568de06dd047aaf1f5cca3c0372%2Fcoverage.json)


## Features

- Utility functions: `add`, `sub`, `square`, `print_data`
- CSV data loading with pandas
- Unit tests with pytest and coverage
- Code quality with ruff (linting + formatting)
- Documentation with Sphinx

## Requirements

- Python 3.11.14
- [uv](https://github.com/astral-sh/uv) (package manager)

## Installation

```bash
uv sync
```

## Usage

```bash
uv run python app/main.py
```

## Run tests

```bash
uv run pytest
```

## Project structure

```
.
├── app/
│   ├── main.py          # Entry point
│   ├── moncsv.csv       # Sample data
│   └── modules/
│       └── mon_module.py  # Core functions
├── tests/
│   └── test_match_csv.py
├── docs/
├── pyproject.toml
└── README.md
```
