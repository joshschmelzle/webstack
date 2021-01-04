import logging

import fastapi
from starlette.requests import Request
from starlette.templating import Jinja2Templates

templates = Jinja2Templates("app/templates")
router = fastapi.APIRouter()
from app.settings import endpoints

log = logging.getLogger("uvicorn")


@router.get("/", include_in_schema=False)
async def index(request: Request):
    data = {"request": request, "endpoints": endpoints}
    return templates.TemplateResponse("home/index.html", data)


@router.get("/favicon.ico", include_in_schema=False)
def favicon():
    return fastapi.responses.RedirectResponse(url="/static/img/favicon.ico")
