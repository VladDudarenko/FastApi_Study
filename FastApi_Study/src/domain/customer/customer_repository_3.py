from sqlalchemy.orm import Session

from src.domain.customer.customer_entity_1 import CustomerEntity
from src.domain.customer.customer_schema_2  import CustomerCreate

class CustomerRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, customer: CustomerCreate) -> CustomerEntity:
        data = customer.model_dump()
        db_customer = CustomerEntity(**data)
        self.db.add(db_customer)
        self.db.commit()
        self.db.refresh(db_customer)
        return db_customer

    def get_all(self):
        return self.db.query(CustomerEntity).all()

    def get_by_id(self, customer_id: int):
        return self.db.query(CustomerEntity).filter(CustomerEntity.id == customer_id).first()
