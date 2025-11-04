from fastapi import FastAPI
from src.core.database_customers_orders import Base, engine
from src.domain.customer.customer_rest_controller_5 import router as customer_router
from src.domain.order.order_rest_controller_5 import router as order_router


Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(customer_router)
app.include_router(order_router)