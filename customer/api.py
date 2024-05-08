from fastapi import FastAPI
from .endpoint import home, cart, order

customer_app = FastAPI()
#商品主界面home、购物车节目cart、订单界面order
customer_app.include_router(home.router, prefix='/home', tags=['customer_home'])
customer_app.include_router(cart.router, prefix='/cart', tags=['customer_cart'])
customer_app.include_router(order.router, prefix='/order', tags=['customer_order'])
