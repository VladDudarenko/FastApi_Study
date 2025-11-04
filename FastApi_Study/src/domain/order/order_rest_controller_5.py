from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from core.database_customers_orders import get_db

from src.domain.order.order_service_4 import OrderService
from src.domain.order.order_schema_2 import Order, OrderCreate


router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=Order)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.create_order(order)

@router.get("/", response_model=List[Order])
def get_orders(db: Session = Depends(get_db)):
    service = OrderService(db)
    return service.repo.get_all()