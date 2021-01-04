from fastapi import APIRouter
from fastapi.responses import JSONResponse

from app.schemas import speedtest

router = APIRouter()


@router.get("/")
async def speedtest(response_model=speedtest.OoklaSpeedtest):
    """
    Run Ookla's `speedtest -f json` and return results

    This will take approximately 30 seconds to return
    """
    results = {}  # await ookla_speedtest_cli_service.get_speedtest_results()

    if "[stderr]" not in results:
        return JSONResponse(content=results, status_code=200)
    else:
        return JSONResponse(
            content={"error": "ERROR: Problem running Ookla speedtest"},
            status_code=503,
        )
