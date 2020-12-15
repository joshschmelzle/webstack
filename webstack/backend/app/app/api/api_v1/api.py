from fastapi import APIRouter

from app.api.api_v1.endpoints import (diagnostics, fpms, network, profiler,
                                      speedtest, utils)

api_router = APIRouter()

api_router.include_router(speedtest.router, prefix="/speedtest", tags=["speedtest"])
api_router.include_router(fpms.router, prefix="/fpms", tags=["front panel menu system"])
api_router.include_router(utils.router, prefix="/utils", tags=["utilities"])
api_router.include_router(
    diagnostics.router, prefix="/diagnostics", tags=["diagnostics"]
)
api_router.include_router(profiler.router, prefix="/profiler", tags=["profiler"])
api_router.include_router(
    network.router, prefix="/network", tags=["network information"]
)
# api_router.include_router(modes.router, prefix="/modes", tags=["modes"])
