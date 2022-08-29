from fastapi import FastAPI

from {{cookiecutter.package_name}}.bootstrap import bootstrap_app, create_context
from {{cookiecutter.package_name}}.config import Config
from {{cookiecutter.package_name}}.context import Context


class TestBootstrap:
    def test_bootsrap_app(self, fixt_config: Config) -> None:
        app = bootstrap_app(fixt_config)
        assert isinstance(app, FastAPI)

    def test_create_context(self, fixt_config: Config) -> None:
        context_1 = create_context(fixt_config, resource_one=None)
        assert isinstance(context_1, Context)

        resource_one = context_1.RESOURCE_ONE
        assert resource_one is not None

        context_2 = create_context(fixt_config, resource_one="RESOURCE_ONE")
        assert isinstance(context_2, Context)

        resource_one = context_2.RESOURCE_ONE
        assert resource_one is not None
