from pydantic import BaseModel
from typing import Optional, List
from domain.order.order_schema_2 import Order

class CustomerCreate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None

class Customer(BaseModel):
    id: Optional[int] = None
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    address: Optional[str]
    orders: List[Order] = []

    class Config:
        from_attributes = True
