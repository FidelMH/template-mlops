check:
	uv run ruff check .
	uv run ruff format --check

fix-lint:
	uv run ruff format
	uv run ruff check --fix

test:
	uv run pytest