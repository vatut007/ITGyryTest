from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from http import HTTPStatus
from schemas.order import OrderItemsCreate, OrderItemsCreateData
from models import OrdersItems, Product, Order
from db.db import get_async_session

router = APIRouter()


@router.post(
    '/add_product',
    response_model=Order,
    description='Принимает ID заказа и ID продукта',
    name='Добавление продукта в заказ'
)
async def add_product_to_order(
    ordersItemsResponse: OrderItemsCreate,
    session: AsyncSession = Depends(get_async_session)
):
    product = await session.execute(
        select(Product).where(
            Product.product_id == ordersItemsResponse.product_id))
    product = product.scalars().first()
    order = await session.execute(
        select(Order).where(Order.order_id == ordersItemsResponse.order_id))
    order = order.scalars().first()
    orderItems = await session.execute(
        select(OrdersItems).where(
            OrdersItems.product_id == ordersItemsResponse.product_id)
    )
    orderItems = orderItems.scalars().first()     
    if not order:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="Заказ с таким ID не найден")
    if not product:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND,
                            detail="Продукт с таким ID не найден")
    if ordersItemsResponse.quantity > product.quantity:
        raise HTTPException(status_code=HTTPStatus.OK,
                            detail="Продукт с таким ID не найден в количестве, указанном в запросе")
    unit_price = product.price
    if orderItems:
        ordersItemsData = OrdersItems(
            **orderItems.model_dump(exclude={"quantity"}),
            quantity=orderItems.quantity + ordersItemsResponse.quantity)
        orderItems.sqlmodel_update(ordersItemsData)
    else:
        orderItems = OrderItemsCreateData(**ordersItemsResponse.model_dump(),
                                          unit_price=unit_price)
        orderItems = OrdersItems.model_validate(orderItems)
    product.sqlmodel_update({
        "quantity": product.quantity-ordersItemsResponse.quantity})
    session.add(product)
    session.add(orderItems)
    await session.commit()
    await session.refresh(order)
    return order
