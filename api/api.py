#在这添加api服务的路由
from fastapi import APIRouter
from api.interface import auth
from api.interface import test

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth")
api_router.include_router(test.router, prefix="/test")
