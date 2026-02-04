from sqlmodel import SQLModel, Field
from typing import Optional


class Category(SQLModel, table=True):
    category_id: Optional[int] = Field(
        default=None,
        primary_key=True,
        nullable=False,
        sa_column_kwargs={"autoincrement": True}
    )
    name: str = Field(
        max_length=255,
        nullable=False
    )
    parent_id: Optional[int] = Field(
        nullable=True,
        foreign_key="category.category_id",
        index=True,
        ondelete="SET NULL"
    )
