from sqlmodel import (CheckConstraint, SQLModel, Field, Relationship, Column,
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
    category: int = Relationship(
        back_populates="product",
        sa_relationship_kwargs={
            "foreign_keys": "[Product.category_id]",
            "ondelete": "RESTRICT"
        }
    )
    __table_args__ = (
        CheckConstraint("quantity > 0",
                        name="ck_product_items_quantity_positive"),
        CheckConstraint("price > 0",
                        name="ck_product_items_price_positive"),
    )
