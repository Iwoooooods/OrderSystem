from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Union

from crud.base import db_servie
from crud.crud_user import crud_get_one_by_condition
from schema.base import UserQuery
from model.base import User

router = APIRouter()

@router.post("/get_one", response_model=UserQuery)
async def get_one_user(condition: Union[dict, None] = None, db: Session = Depends(db_servie.get_db)):
    if condition:
        user = crud_get_one_by_condition(condition, db)
    else:
        user = db.query(User).first()
    return user

@router.get("/hello", response_model=str)
async def test():
    return "test!test!"