import traceback

from sqlalchemy import and_
from sqlalchemy.orm import Session
from typing import Union
from loguru import logger

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

def crud_add_user(db: Session, user: User) -> User:
    print(f'name: {user.user_name}+email: {user.email}')
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def crud_delete_user(db: Session, user: User) -> None:
    try:
        db.delete(user)
        db.commit()
        logger.info('user deleted')
    except Exception as e:
        db.rollback()
        logger.error(traceback.format_exc())
        raise e
    return None



if __name__ == '__main__':
    from base import db_servie
    session = next(db_servie.get_db())
    crud_add_user((session), User(user_name='merchant', email='15388014287@163.com', pwd='welcome'))
    result = crud_get_multi_by_condition(session)
    for res in result:
        print(f'{res.to_dict()}')