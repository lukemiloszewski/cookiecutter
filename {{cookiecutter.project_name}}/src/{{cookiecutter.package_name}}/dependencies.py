from fastapi import Request

from {{cookiecutter.package_name}}.context import Context


def get_context(request: Request) -> Context:
    """Intercepts the application state from a request and returns the associated Context object.

    Args:
        request (Request): a request made to an endpoint.

    Returns:
        Context: a data structure to store application resources.
    """
    context = request.app.state.context
    return context
