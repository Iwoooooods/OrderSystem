from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from customer.service.product_service import product_service
from schema.page import MyPage
from crud.base import db_servie

router = APIRouter()

@router.get("/") # 商城主界面，按页返回商品
async def home(api_in: MyPage, db: Session = Depends(db_servie.get_db)):
    return product_service.get_home_product(api_in, db)

@router.get("/detail") # 查看商品详情
async def detail():
    pass

@router.post("/add_to_cart") # 加入购物车
async def add_to_cart():
    pass

@router.get("/go_cart") # 查看购物车
async def go_cart():
    pass

@router.post("/purchase") # 直接购买商品
async def purchase():
    pass
