from sqlalchemy.orm import Session

from .customer_repository_3 import CustomerRepository
from .customer_schema_2 import CustomerCreate,Customer


class CustomerService:
    def __init__(self, db: Session):
        self.repo = CustomerRepository(db)

    def register_customer(self, customer: CustomerCreate) -> Customer:
        #Logik
        return self.repo.create(customer)

    def get_customer_with_orders(self, customer_id: int):
        return self.repo.get_by_id(customer_id)