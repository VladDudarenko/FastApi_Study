from sqlalchemy.orm import Session

from src.domain.order.order_entity_1 import OrderEntity
from src.domain.order.order_schema_2 import OrderCreate

class OrderRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, order: OrderCreate) -> OrderEntity:
        db_order = OrderEntity(**order.model_dump())
        self.db.add(db_order)
        self.db.commit()
        self.db.refresh(db_order)
        return db_order

    def get_all(self):
        return self.db.query(OrderEntity).all()