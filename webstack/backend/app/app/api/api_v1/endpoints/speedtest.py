import json
import logging

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas import speedtest
from app.services import ookla_speedtest_cli_service

router = APIRouter()

log = logging.getLogger("uvicorn")


@router.get("/ookla", response_model=speedtest.OoklaSpeedtest)
async def run_ookla_speedtest():
    """
    Run Ookla Speedtest CLI (`speedtest -f json`) and return results.

    Note this will take approximately 30 seconds to return.
    """
    resp = await ookla_speedtest_cli_service.get_speedtest_results()

    if "[stderr]" not in resp:
        results = json.loads(resp)
        return JSONResponse(content=results, status_code=200)
    else:
        log.error(" ".join(resp.split("\n")))
        return JSONResponse(
            content={"error": "ERROR: Problem running Ookla speedtest"},
            status_code=503,
        )
