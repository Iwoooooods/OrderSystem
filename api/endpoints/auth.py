from fastapi import Depends, APIRouter, Form
from sqlalchemy.orm import Session

from schema.base import UserQuery, LoginForm
from api.service.auth_service import auth_service
from crud.base import db_servie

router = APIRogit uter()

@router.post('/login', response_model=list[str])
async def login(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.authenticate(form, db)

@router.put('register', response_model=str)
async def register(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.register(form, db)
