"""Импорты класса Base и всех моделей для Alembic."""
from sqlmodel import SQLModel # noqa
from src.models.ordersItems import OrdersItems # noqa
from src.models.categories import Category # noqa
from src.models.clients import Client # noqa
from src.models.orders import Order # noqa
from src.models.product import Product # noqa
