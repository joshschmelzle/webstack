import json

from fastapi import APIRouter

from .helpers import run

router = APIRouter()


@router.get("/")
async def ookla_speedtest():
    """
    Run `speedtest-cli --json` and return results
    """
    results = json.dumps(json.loads(await run("speedtest-cli --json")))

    if "[stderr]" not in results:
        return results
    else:
        results = "Problem running speedtest-cli --json"
