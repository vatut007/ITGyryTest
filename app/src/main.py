from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.settings import settings

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/v1',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
)