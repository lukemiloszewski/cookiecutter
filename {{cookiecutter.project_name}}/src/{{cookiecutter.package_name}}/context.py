from enum import Enum
from typing import Any, Dict, Union


class Context:
    """A data structure to store application resources."""

    def __init__(self, resources: Union[Dict[str, Any], None] = None):
        if resources is None:
            resources = {}
        super().__setattr__("_resources", resources)

    def __setattr__(self, key: Any, value: Any) -> None:
        self._resources[key] = value

    def __getattr__(self, key: Any) -> Any:
        try:
            return self._resources[key]
        except KeyError:
            message = "'{}' object has no attribute '{}'"
            raise AttributeError(message.format(self.__class__.__name__, key))

    def __delattr__(self, key: Any) -> None:
        del self._resources[key]


class Resource(str, Enum):
    """A mapping of resource names used within the application."""

    RESOURCE_ONE = "RESOURCE_ONE"

    def __str__(self) -> str:
        return str.__str__(self)
