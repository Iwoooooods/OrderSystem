from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import Union

from model.base import User

def crud_get_multi_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(User)
    if condition:
        filters = [getattr(User, key) == value for key, value in condition.items() if hasattr(User, key)]
        query = query.filter(and_(*filters))
    return query.all()

def crud_get_one_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(User)
    if condition:
        filters = [getattr(User, key) == value for key, value in condition.items() if hasattr(User, key)]
        query = query.filter(and_(*filters))
    return query.first()

if __name__ == '__main__':
    from base import db_servie
    result = crud_get_multi_by_condition(next(db_servie.get_db()))
    for res in result:
        print(res.to_dict())