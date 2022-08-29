{% if cookiecutter.use_cli == "yes" -%}
import pytest
from typer.testing import CliRunner
{% endif -%}

{% if cookiecutter.use_api == "yes" -%}
import functools
from typing import Any, Callable, Iterator

import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from {{cookiecutter.package_name}}.app import create_app
from {{cookiecutter.package_name}}.bootstrap import create_context
from {{cookiecutter.package_name}}.config import Config
from {{cookiecutter.package_name}}.context import Context
{% endif -%}


{% if cookiecutter.use_cli == "yes" -%}
@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()
{% endif -%}

{% if cookiecutter.use_api == "yes" -%}
@pytest.fixture
def fixt_config() -> Config:
    config = Config(GREETING="HELLO, TEST WORLD!")
    return config


@pytest.fixture
def fixt_resource_one() -> Any:
    resource_one = None
    return resource_one


@pytest.fixture
def fixt_context(fixt_config: Config, fixt_resource_one: Any) -> Context:
    context = create_context(fixt_config, resource_one=fixt_resource_one)
    return context


@pytest.fixture
def fixt_app(fixt_context: Context) -> FastAPI:
    app = create_app(fixt_context)
    return app


@pytest.fixture
def fixt_client(fixt_app: FastAPI) -> Iterator[TestClient]:
    with TestClient(fixt_app) as client:
        yield client


@pytest.fixture
def test_client_factory(app: FastAPI) -> Callable[..., TestClient]:
    return functools.partial(TestClient, app)
{% endif -%}
