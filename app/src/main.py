from contextlib import asynccontextmanager
import logging
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from core.settings import settings
from api.routers import main_router
from utils.add_data_db import add_data_db

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await add_data_db()
    yield

app = FastAPI(
    title=settings.project_name,
    docs_url='/api/v1/docs',
    openapi_url='/api/openapi.json',
    default_response_class=ORJSONResponse,
    lifespan=lifespan
)

app.include_router(main_router)
