from fastapi import APIRouter, Depends
from  sqlalchemy.orm import Session

from src.core.database_customers_orders import get_db
from src.domain.customer.customer_service_4 import CustomerService
from src.domain.customer.customer_schema_2 import Customer, CustomerCreate


router = APIRouter(prefix="/customer", tags=["Customer"])


@router.post("/", response_model=Customer)
async def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.register_customer(customer)

@router.get("/{customer_id}", response_model=Customer)
async def get_customers(customer_id: int, db: Session = Depends(get_db)):
    service = CustomerService(db)
    return service.get_customer_with_orders(customer_id)