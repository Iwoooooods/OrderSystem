from fastapi import Depends, APIRouter, Form
from sqlalchemy.orm import Session

from schema.user_schema import UserQuery, LoginForm
from api.service.auth_service import auth_service
from crud.base import db_servie

router = APIRouter()

# 注册和登录正确的返回都应该是商品主界面的商品dict数据
@router.post('/login', response_model=dict)
async def login(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.login(db, form)


@router.put('/register')
async def register(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.register(db, form)

