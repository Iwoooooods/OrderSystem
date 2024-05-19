from fastapi import APIRouter
from .endpoint import home, order

merch_router = APIRouter()
#商品主界面home、购物车节目cart、订单界面order
merch_router.include_router(home.router, prefix='/home', tags=["merchant"])
merch_router.include_router(order.router, prefix='/order', tags=["merchant"])
