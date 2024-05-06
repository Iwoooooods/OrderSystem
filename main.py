from fastapi import FastAPI
from api.api import api_router

def get_application():
    app = FastAPI()
    return app

from customer.api import customer_app
from merchant.api import merchant_app
app = get_application()
app.include_router(api_router)
app.mount('/customer', customer_app)
app.mount('/merchant', merchant_app)

# 设置中间件
from middleware import token, logging
app.middleware('http')(logging.logging)
app.add_middleware(token.TokenMiddleware, skip_paths=['/']) # debug环境测试
# app.add_middleware(token.TokenMiddleware, skip_paths=['/openapi.json','/auth/login','/test/','/docs','/auth/register'])

@app.get("/")
async def root():
    return {"message": "Hello!"}

@app.on_event('startup')
async def on_startup():
    await logging.create_log_file()
    from crud.base import db_servie
    db_servie.init_db()
