from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session

from core.database import get_db
from domain.customer.customer_service_4 import CustomerService
from domain.customer.customer_schema_2 import Customer, CustomerCreate


router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.register_customer(customer)

@router.get("/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_customer_with_orders(customer_id)