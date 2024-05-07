from typing import List

from fastapi import Depends, APIRouter, Form
from sqlalchemy.orm import Session

from schema.base import UserQuery, LoginForm
from model.base import User
from api.service.auth_service import auth_service
from crud.base import db_servie
from crud.crud_user import crud_get_one_by_condition

router = APIRogit uter()

# 注册和登录正确的返回都应该是商品主界面的商品dict数据
@router.post('/login', response_model=dict)
async def login(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.login(db, form)


@router.put('/register', response_model=dict)
async def register(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.register(db, form)
