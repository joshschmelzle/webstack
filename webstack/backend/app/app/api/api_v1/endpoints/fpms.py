import logging

import fastapi
from fastapi import APIRouter

from app.schemas import fpms
from app.services import systemsummary_service

router = APIRouter()

log = logging.getLogger("uvicorn")


@router.get("/system_summary", response_model=fpms.SystemSummary)
async def show_system_summary():
    """
    Returns device status information:

    - IP address
    - CPU utilization
    - Memory usage
    - Disk utilization
    - Device temperature
    """
    try:
        return await systemsummary_service.get_system_summary_async()
    except Exception as x:
        log.info(x)
        return fastapi.Response(content=str(x), status_code=500)
