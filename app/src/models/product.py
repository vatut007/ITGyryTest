from sqlmodel import (CheckConstraint, ForeignKeyConstraint, SQLModel, Field,
                      Column,
                      DECIMAL)
from decimal import Decimal
from typing import Optional


class Product(SQLModel, table=True):
    product_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True}
    )
    name: str = Field(
        max_length=255,
        nullable=False
    )
    quantity: int = Field(
        nullable=False,
        ge=0
    )
    price: Decimal = Field(
        sa_column=Column(DECIMAL(10, 2), nullable=False),
        gt=0
    )
    category_id: int = Field(
        nullable=False,
        foreign_key="category.category_id",
        index=True
    )
    __table_args__ = (
        CheckConstraint("quantity > 0",
                        name="ck_product_items_quantity_positive"),
        CheckConstraint("price > 0",
                        name="ck_product_items_price_positive"),
        ForeignKeyConstraint(
            ['category_id'], ['category.category_id'],
            name='fk_orders_client',
            ondelete='RESTRICT')
    )
