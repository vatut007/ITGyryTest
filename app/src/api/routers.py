from fastapi import APIRouter
from api.endpoints import order_router

main_router = APIRouter(prefix='/v1')
main_router.include_router(order_router)
