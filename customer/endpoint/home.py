from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from customer.service.product_service import product_service
from schema.product_schema import ProductQuery
from crud.base import db_servie

router = APIRouter()

@router.post("/") # 商城主界面，按页返回商品
async def home(api_in: ProductQuery, db: Session = Depends(db_servie.get_db)):
    return await product_service.get_home_product(api_in, db)

@router.get("/detail") # 查看商品详情
async def detail(id: int, db: Session = Depends(db_servie.get_db)):
    return await product_service.get_product_detail(id, db)

@router.get("/add_to_cart") # 加入购物车
async def add_to_cart(user_id: int, product_id: int, db: Session = Depends(db_servie.get_db)):
    await product_service.add_to_cart(user_id, product_id, db)

@router.get("/go_cart") # 查看购物车
async def go_cart():
    pass

@router.post("/purchase") # 直接购买商品
async def purchase():
    pass
