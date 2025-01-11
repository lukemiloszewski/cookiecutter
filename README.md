<h1 align="center">Cookiecutter</h1>
<p align="center">A modern package template based on python best practices 🐍</p>

## Overview

* [Make](https://www.gnu.org/software/make/) - build automation
* [Poetry](https://python-poetry.org) - dependency management and packaging
* [Pytest](https://docs.pytest.org/en/stable/), [Pytest-Cov](https://pytest-cov.readthedocs.io/en/latest/) - testing and coverage reports
* [Typer](https://typer.tiangolo.com/) - CLI
* [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) - documentation
* [Ruff](https://docs.astral.sh/ruff/) - code formatting
* [Mypy](https://mypy.readthedocs.io/en/stable/), [Typeguard](https://github.com/agronholm/typeguard) - type checking
* [GitHub Actions](https://docs.github.com/en/actions) - continuous integration and deployment
* [Dependabot](https://docs.github.com/en/code-security/dependabot) - automated dependency updates
* [GitHub Labeler](https://github.com/marketplace/actions/github-labeler) - automated label management
* [Release Drafter](https://github.com/marketplace/actions/release-drafter) - automated release notes

This template supports Python 3.12.x.

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
* `use_docs` - include template for documentation
* `use_github_actions` - include workflows for continuous integration
