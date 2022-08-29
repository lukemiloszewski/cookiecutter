import json
import logging
import sys


JSON_FORMAT = json.dumps(
    {
        "time": "%(asctime)s",
        "level": "%(levelname)s",
        "module": "%(module)s",
        "line": "%(lineno)d",
        "message": "%(message)s",
    }
)


def configure_logging() -> None:
    """Configures the root and external loggers of the application."""
    json_formatter = logging.Formatter(JSON_FORMAT)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(json_formatter)
    console_handler.setLevel(logging.INFO)

    logging.getLogger("uvicorn.access").propagate = False
    logging.getLogger("uvicorn.error").propagate = False
    logging.getLogger("uvicorn.access").handlers.clear()
    logging.getLogger("uvicorn.error").handlers.clear()

    logger = logging.getLogger()
    logger.handlers.clear()
    logger.addHandler(console_handler)
    logger.setLevel(logging.INFO)


async def log_startup() -> None:
    """Banner logged on application startup."""
    logging.info("Application starting up!")
    return None


async def log_shutdown() -> None:
    """Banner logged on application shutdown."""
    logging.info("Application shutting down!")
    return None
