from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel


class Order(SQLModel, table=True):
    order_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True}
    )
    client_id: int = Field(
        nullable=False,
        foreign_key="client.client_id",
        index=True
    )
    order_date: datetime = Field(
        default=datetime.now(),
        nullable=False
    )

    client: int = Relationship(
        back_populates="order",
        sa_relationship_kwargs={
            "foreign_keys": "[Order.client_id]",
            "ondelete": "RESTRICT"
        }
    )
