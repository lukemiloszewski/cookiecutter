"""Composition root of the application."""

from typing import Any

from fastapi import FastAPI

from {{cookiecutter.package_name}}.app import create_app
from {{cookiecutter.package_name}}.config import Config
from {{cookiecutter.package_name}}.context import Context, Resource
from {{cookiecutter.package_name}}.logging import configure_logging


def bootstrap_app(config: Config) -> FastAPI:
    """Returns a fully-configured application instance.

    Args:
        config (Config): the environment configuration.

    Returns:
        FastAPI: the application instance.
    """
    configure_logging()
    context = create_context(config)
    app = create_app(context)
    return app


def create_context(config: Config, resource_one: Any = None) -> Context:
    """Returns a data structure used to store application resources.

    Args:
        config (Config): the environment configuration.
        resource_one (Any): an application resource.

    Returns:
        Context: a data structure to store application resources.
    """
    resources = {}

    if resource_one is None:
        resource_one = config.GREETING

    resources[Resource.RESOURCE_ONE.value] = resource_one

    context = Context(resources)
    return context
