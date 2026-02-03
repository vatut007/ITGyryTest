from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from schemas.order import OrderItemsCreate, OrderItemsCreateData
from models.ordersItems import OrdersItems
from models.product import Product
from models.orders import Order
from db.db import get_async_session

router = APIRouter()


@router.post(
    '/add_product',
    response_model=Order,
    description='Принимает ID заказа и ID продукта',
    name='Добавление продукта в заказ'
)
async def add_product_to_order(
    ordersItems: OrderItemsCreate,
    session: AsyncSession = Depends(get_async_session)
):
    product = await session.execute(
        select(Product).where(Product.product_id == ordersItems.product_id))
    product = product.scalars().first()
    if not product:
        raise HTTPException(status_code=404, detail="Продукт с таким ID не найден")
    unit_price = product.price
    ordersItems = OrderItemsCreateData(**ordersItems.model_dump(),
                                       unit_price=unit_price)
    order = OrdersItems.model_validate(OrdersItems)
    session.add(order)
    await session.commit()
    await session.refresh(order)
    return order
