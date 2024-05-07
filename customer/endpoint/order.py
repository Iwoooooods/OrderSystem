from fastapi import APIRouter

router = APIRouter()

@router.get("/") # 订单主界面
async def home():
    pass

@router.post("/refund") # 向商家发送消息表示退款
async def refund():
    pass

@router.get("/detail")
async def detail():
    pass