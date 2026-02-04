from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.settings import settings
from api.routers import main_router

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/v1/docs',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)

app.include_router(main_router)
