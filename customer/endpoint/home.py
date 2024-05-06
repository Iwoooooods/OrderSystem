from fastapi import APIRouter

router = APIRouter()

@router.get("/") # 商城主界面
async def home():
    pass

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
