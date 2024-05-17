from fastapi import APIRouter
from customer.endpoint import home, cart, order

cust_router = APIRouter()
#商品主界面home、购物车节目cart、订单界面order
cust_router.include_router(home.router, prefix='/home', tags=['customer'])
cust_router.include_router(cart.router, prefix='/cart', tags=['customer'])
cust_router.include_router(order.router, prefix='/order', tags=['customer'])
