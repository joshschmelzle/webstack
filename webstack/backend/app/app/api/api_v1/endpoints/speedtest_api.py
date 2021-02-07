import json
import logging

from fastapi import APIRouter, Response

from app.models.validation_error import ValidationError
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
    try:
        resp = await ookla_speedtest_cli_service.get_speedtest_results()
        return json.loads(resp)
    except ValidationError as ve:
        return Response(content=ve.error_msg, status_code=ve.status_code)
    except Exception as ex:
        return Response(content=str(ex), status_code=500)
