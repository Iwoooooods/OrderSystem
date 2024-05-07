from fastapi import FastAPI
from endpoint import home, cart, order

customer_app = FastAPI()
#商品主界面home、购物车节目cart、订单界面order
customer_app.include_router(home.router, prefix='/home')
customer_app.include_router(cart.router, prefix='/cart')
customer_app.include_router(order.router, prefix='/order')
