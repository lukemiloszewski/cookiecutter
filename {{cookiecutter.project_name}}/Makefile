init:
	poetry config virtualenvs.in-project true
	poetry install
	poetry run pre-commit install --hook-type pre-commit --install-hooks

test:
	poetry run pytest tests -v --cov

{% if cookiecutter.use_api == "yes" -%}
app:
	poetry run python scripts/main.py

{% endif -%}
{% if cookiecutter.use_auto_publish == "yes" -%}
publish:
	poetry publish --build

{% endif -%}
{% if cookiecutter.use_docs == "yes" -%}
doc:
	poetry run mkdocs serve

{% endif -%}
requirements:
	poetry export -f requirements.txt --output requirements.txt

flake8:
	poetry run flake8 src tests

mypy:
	poetry run mypy src tests

pydocstyle:
	poetry run pydocstyle src

isort:
	poetry run isort src tests

black:
	poetry run black src tests

safety:
	poetry export -f requirements.txt --with dev --without-hashes | safety check --stdin

bandit:
	poetry run bandit -r src

lint: flake8 mypy pydocstyle

format: isort black

pre-commit:
	poetry run pre-commit run --all-files --color=always
