from decimal import Decimal
from sqlmodel import DECIMAL, CheckConstraint, Column, Field, SQLModel


class OrdersItems(SQLModel, table=True):
    order_item_id: int = Field(primary_key=True,
                               sa_column_kwargs={"autoincrement": True})
    order_id: int = Field(nullable=False)
    product_id: int = Field(nullable=False)
    quantity: int = Field(sa_column=Column(DECIMAL(10, 2), nullable=False))
    unit_price: Decimal = Field(nullable=False, gt=0)
    __table_args__ = (
        CheckConstraint("quantity > 0",
                        name="ck_orders_items_quantity_positive"),
        CheckConstraint("unit_price > 0",
                        name="ck_orders_items_unit_price_positive"),
    )
