from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.core.database_customers_orders import Base

class CustomerEntity(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    phone = Column(String, index=True)
    address = Column(String, index=True)

    orders = relationship("OrderEntity", back_populates="customer")


