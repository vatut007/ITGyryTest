from sqlmodel import ForeignKeyConstraint, SQLModel, Field
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
        index=True
    )
    __table_args__ = (
        ForeignKeyConstraint(
             ["parent_id"],
             ["category.category_id"],
             name="fk_categories_parent",
             ondelete="SET NULL"
             ),
    )
