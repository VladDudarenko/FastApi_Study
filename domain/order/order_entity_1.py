from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from core.database import Base

class OrderEntity(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    item = Column(String, index=True)
    price = Column(Integer)
    place = Column(String)
    customer_id = Column(Integer, ForeignKey('customers.id')) # ForeignKey -> customer_entity:customers.id

    customer = relationship("CustomerEntity", back_populates="orders")