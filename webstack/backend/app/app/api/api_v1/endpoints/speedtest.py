import json

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from .helpers import run

router = APIRouter()


@router.get("/")
async def speedtest():
    """
    Run `speedtest-cli --json` and return results
    """
    results = json.loads(await run("speedtest-cli --json"))

    if "[stderr]" not in results:
        return JSONResponse(content=results,status_code=200)
    else:
        return JSONResponse(content={"error": "ERROR: Problem running speedtest-cli --json"}, status_code=503)
