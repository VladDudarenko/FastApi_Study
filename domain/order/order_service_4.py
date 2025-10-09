from sqlalchemy.orm import Session

from .order_repository_3 import OrderRepository
from .order_schema_2 import OrderCreate

class OrderService:
    def __init__(self, db: Session):
        self.repo = OrderRepository(db)

    def create_order(self, order: OrderCreate):
        return self.repo.create(order)