from fastapi import FastAPI
from endpoint import home, order

merchant_app = FastAPI()
#商品主界面home、购物车节目cart、订单界面order
merchant_app.include_router(home.router, prefix='/home')
merchant_app.include_router(order.router, prefix='/order')
