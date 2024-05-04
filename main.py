from fastapi import FastAPI
from api.api import api_router


def get_application():
    app = FastAPI()
    return app

app = get_application()
app.include_router(api_router)
# 设置中间件
from middleware import token, logging
app.add_middleware(token.TokenMiddleware, skip_paths=['/openapi.json','/auth/login','/test/','/docs'])
app.middleware('http')(logging.logging)

@app.get("/")
async def root():
    return {"message": "Hello!"}

@app.on_event('startup')
async def on_startup():
    print("startup")
    from crud.base import db_servie
    db_servie.init_db()
    print("startup finished")
