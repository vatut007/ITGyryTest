from pydantic import BaseModel, Field


class OrderItemsCreate(BaseModel):
    order_id: int = Field()
    product_id: int = Field()
    quantity: int = Field()


class OrderItemsCreateData(OrderItemsCreate):
    unit_price: float = Field()
    
