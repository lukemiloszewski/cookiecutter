from fastapi import FastAPI

from {{cookiecutter.package_name}} import __DESCRIPTION__, __TITLE__, __VERSION__
from {{cookiecutter.package_name}}.context import Context
from {{cookiecutter.package_name}}.logging import log_shutdown, log_startup
from {{cookiecutter.package_name}}.middleware import exception_middleware, time_middleware
from {{cookiecutter.package_name}}.routers import health_router, tags


def create_app(context: Context) -> FastAPI:
    """Returns an application instance.

    Args:
        context (Context): a data structure to store application resources.

    Returns:
        FastAPI: the application instance.
    """
    app = FastAPI(
        title=__TITLE__,
        description=__DESCRIPTION__,
        version=__VERSION__,
        openapi_tags=[tags.TAG_GENERAL],
    )

    app.include_router(health_router.router, prefix="")

    app.middleware("http")(exception_middleware)
    app.middleware("http")(time_middleware)

    app.on_event("startup")(log_startup)
    app.on_event("shutdown")(log_shutdown)

    app.state.context = context
    return app
