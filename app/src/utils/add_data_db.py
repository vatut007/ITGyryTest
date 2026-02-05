import contextlib
from decimal import Decimal
import logging

from sqlalchemy import select
from db.db import get_async_session
from models import Category, Product, Client, Order
from datetime import datetime


get_async_session_context = contextlib.asynccontextmanager(get_async_session)
logger = logging.getLogger(__name__)


async def add_data_db():
    async with get_async_session_context() as session:
        result = await session.execute(
                select(1).select_from(Order).limit(1)
            )
        exists = result.scalars().first() is not None
        if exists:
            logger.info('Заказ в БД уже существует')
            return
        category = Category(name='Колбасы', parent_id=None)
        session.add(category)
        await session.commit()
        await session.refresh(category)
        if not category.category_id:
            raise Exception('Category has not category_id')
        client = Client(name='pol', address=None)
        product = Product(name='Колбаса варенная',
                          quantity=50,
                          price=Decimal(500),
                          category_id=category.category_id)
        session.add(client)
        session.add(product)
        await session.commit()
        await session.refresh(client)
        await session.refresh(product)
        if not client.client_id:
            raise Exception('Category has not category_id')
        order = Order(client_id=client.client_id, order_date=datetime.now())
        session.add(order)
        await session.commit()
