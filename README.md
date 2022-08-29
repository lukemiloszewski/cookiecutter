<h1 align="center">Cookiecutter</h1>
<p align="center">A modern template based on python best practices 🐍</p>

## Overview

* [Make](https://www.gnu.org/software/make/) - build automation
* [Poetry](https://python-poetry.org) - dependency management and packaging
* [Pre-Commit](https://pre-commit.com) - git hooks
* [Pytest](https://docs.pytest.org/en/stable/), [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/) - testing and coverage reports
* [FastAPI](https://fastapi.tiangolo.com/) - API
* [Typer](https://typer.tiangolo.com/) - CLI
* [Black](https://black.readthedocs.io/en/stable/), [Isort](https://pycqa.github.io/isort/) - code formatting
* [Flake8](https://flake8.pycqa.org/en/latest/), [Mypy](https://mypy.readthedocs.io/en/stable/), [Pydocstyle](https://www.pydocstyle.org/en/stable/) - code linting
* [GitHub Actions](https://docs.github.com/en/actions) - continuous integration and deployment
* [Dependabot](https://docs.github.com/en/code-security/dependabot) - automated dependency updates
* [GitHub Labeler](https://github.com/marketplace/actions/github-labeler) - automated label management
* [Release Drafter](https://github.com/marketplace/actions/release-drafter) - automated release notes

This template supports Python 3.8.x, 3.9.x and 3.10.x.

## Usage

### Requirements

* [Cookiecutter](https://cookiecutter.readthedocs.io/en/stable/)
* [Make](https://www.gnu.org/software/make/)
* [Poetry](https://python-poetry.org)

### Installation

```shell
cookiecutter gh:lukemiloszewski/cookiecutter
```

### Configuration

* `project_name` - project name
* `package_name` - package name
* `package_version` - package version
* `package_description` - package description
* `github_homepage` - GitHub homepage where the project is hosted
* `author_name` - author name
* `author_email` - author email
* `use_api` - include template for an API
* `use_cli` - include template for a CLI
* `use_auto_publish` - include GitHub Action workflow for automatic publishing to PyPI
* `use_github_actions` - include GitHub Action workflow for CI/CD
* `use_git` - initialize git repository and make initial commit
