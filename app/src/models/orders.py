from datetime import datetime
from typing import Optional
from sqlmodel import Field, ForeignKeyConstraint, SQLModel


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
    __table_args__ = (
        ForeignKeyConstraint(
            ['client_id'],
            ['client.client_id'],
            name='fk_orders_client',
            ondelete='RESTRICT'),
    )
