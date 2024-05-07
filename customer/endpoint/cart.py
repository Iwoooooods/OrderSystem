from fastapi import APIRouter

router = APIRouter()

@router.get("/") # 购物车主页面
async def home():
    pass

@router.post("/purchase") # 下单
async def purchase():
    pass

@router.post("/delete") # 删除商品
async def delete():
    pass

@router.post("/update") # 更改商品数量
async def update():
    pass

@router.get("/detail") # 查看商品详情
async def detail():
    pass
