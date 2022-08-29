from fastapi import FastAPI, Request

from {{cookiecutter.package_name}}.context import Context
from {{cookiecutter.package_name}}.dependencies import get_context


class TestDependencies:
    def test_get_context(self, fixt_app: FastAPI) -> None:
        request = Request(scope={"type": "http", "app": fixt_app})

        context = get_context(request)

        assert isinstance(context, Context)
