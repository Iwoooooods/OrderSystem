#在这添加api服务的路由
from fastapi import APIRouter
from api.endpoints import auth
from api.endpoints import test

api_router = APIRouter()
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(test.router, prefix="/test", tags=["test"])
