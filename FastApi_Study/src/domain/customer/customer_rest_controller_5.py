from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session
from typing import List

from src.core.database_customers_orders import get_db
from src.domain.customer.customer_service_4 import CustomerService
from src.domain.customer.customer_schema_2 import Customer, CustomerCreate


router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.register_customer(customer)

@router.get("/customers", response_model=List[Customer])
async def get_customers(db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_all_customers()

@router.get("/{customer_id}", response_model=Customer)
async def get_customers_by_id(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_customer_with_orders(customer_id)
