from typing import Optional
from sqlmodel import Field, SQLModel


class Client(SQLModel, table=True):
    client_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True}
    )
    name: str = Field(
        max_length=255,
        nullable=False
    )
    address: Optional[str] = Field(
        max_length=500,
        nullable=True
    )
