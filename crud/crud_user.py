from sqlalchemy.orm import Session

from model.base import User

def crud_get_multi_by_condition(condition: dict, db: Session):
    print(f'get by: {condition}')
    query = db.query(User)
    for key, value in condition.items():
        query = query.filter(getattr(User, key) == value)
    return query.all()

def crud_get_one_by_condition(condition: dict, db: Session):
    print(f'get by: {condition}')
    query = db.query(User)
    for key, value in condition.items():
        query = query.filter(getattr(User, key) == value)
    return query.first()