import logging
import time
from typing import Any, Callable

from fastapi import Request
from fastapi.responses import JSONResponse


async def exception_middleware(request: Request, call_next: Callable[..., Any]) -> Any:
    """Middleware to handle uncaught exceptions."""
    try:
        return await call_next(request)
    except Exception as exc:
        exc_msg = f"{type(exc).__name__} caught by middleware: {str(exc)}"
        logging.error(exc_msg)
        return JSONResponse(
            status_code=500,
            content={"message": exc_msg},
        )


async def time_middleware(request: Request, call_next: Callable[..., Any]) -> Any:
    """Middleware to log request times."""
    logging.info(
        f"Request started: Request type = {request.method}, Request path = {request.url.path}"
    )
    start_time = time.time()
    response = await call_next(request)
    end_time = time.time() - start_time
    formatted_end_time = "{0:.2f}".format(end_time)
    logging.info(
        f"Request finished: Status code = {response.status_code}, Duration = {formatted_end_time}s"
    )
    return response
