from fastapi import Depends, APIRouter, Form
from sqlalchemy.orm import Session

from schema.base import UserQuery, LoginForm
from api.service.auth_service import auth_service
from crud.base import db_servie

router = APIRouter()

@router.post('/login', response_model=list[UserQuery])
def login(form: LoginForm, db: Session = Depends(db_servie.get_db)):
    return auth_service.authenticate(form, db)
