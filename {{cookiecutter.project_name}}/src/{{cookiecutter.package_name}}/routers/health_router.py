from typing import Dict

from fastapi import APIRouter, Depends

from {{cookiecutter.package_name}}.context import Context
from {{cookiecutter.package_name}}.dependencies import get_context
from {{cookiecutter.package_name}}.routers.tags import TAG_GENERAL


router = APIRouter()


@router.get("/", summary="Health check", tags=[TAG_GENERAL["name"]])
async def get_health_payload(context: Context = Depends(get_context)) -> Dict[str, str]:
    """Endpoint to monitor whether the service is running."""
    return {"message": f"{context.RESOURCE_ONE}"}
