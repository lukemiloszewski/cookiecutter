init:
	poetry config virtualenvs.in-project true
	poetry install --all-extras --sync

test:
	poetry run pytest tests -v --cov

publish:
	poetry publish --build

{% endif -%}
{% if cookiecutter.use_docs == "yes" -%}
doc:
	poetry run mkdocs serve

{% endif -%}
requirements:
	poetry export -f requirements.txt --output requirements.txt

lint:
	poetry run mypy src tests
	poetry run pydocstyle src
	poetry run ruff check src tests
	poetry run ruff format src tests --check

format:
	poetry run ruff check src tests --fix
	poetry run ruff format src tests
