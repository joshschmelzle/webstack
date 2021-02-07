import json
import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas import fpms
from app.services import fpms_service

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
    resp = await fpms_service.get_system_summary()

    if "[stderr]" not in resp:
        results = json.loads(resp)
        return JSONResponse(content=results, status_code=200)
    else:
        error = " ".join(resp.split("\n"))
        log.error(error)
        return JSONResponse(
            content={"error": f"ERROR: {error}"},
            status_code=503,
        )
