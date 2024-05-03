from fastapi import FastAPI
from api.api import api_router


def get_application():
    app = FastAPI()
    return app

app = get_application()
app.include_router(api_router)
from middleware.token import TokenMiddleware
app.add_middleware(TokenMiddleware, skip_paths=['/openapi.json','/auth/login','/test/','/docs'])

@app.get("/")
def root():
    return {"message": "Hello!"}

@app.on_event('startup')
def on_startup():
    print("startup")
    from crud.base import db_servie
    db_servie.init_db()
    print("startup finished")