from typing import Any

import pytest
from fastapi import Request
from fastapi.responses import JSONResponse

from {{cookiecutter.package_name}}.middleware import exception_middleware


@pytest.fixture(scope="module")
def fixt_request() -> Request:
    request = Request(scope={"type": "http"})
    return request


class TestMiddleware:
    @pytest.mark.asyncio
    async def test_exception_middleware(self, fixt_request: Request) -> None:
        async def call_next_func(request: Request) -> Any:
            raise ValueError("Test error!")

        resp = await exception_middleware(request=fixt_request, call_next=call_next_func)

        assert isinstance(resp, JSONResponse)
        assert resp.status_code == 500
