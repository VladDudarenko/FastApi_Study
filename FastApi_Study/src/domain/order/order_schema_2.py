from typing import Optional
from pydantic import BaseModel

class OrderCreate(BaseModel):
    item: Optional[str] = None
    price: Optional[int] = None
    place: Optional[str] = None
    customer_id: Optional[int] = None

class Order(BaseModel):
    id: Optional[int] = None
    item: Optional[str] = None
    price: Optional[int] = None
    place: Optional[str] = None
    customer_id: Optional[int] = None

    class Config:
        from_attributes = True
