from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import Union

from model.base import Product

def crud_get_multi_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(Product)
    if condition:
        filters = [getattr(Product, key) == value for key, value in condition.items() if hasattr(Product, key)]
        query = query.filter(and_(*filters))
    return query.all()

def crud_get_one_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(Product)
    if condition:
        filters = [getattr(Product, key) == value for key, value in condition.items() if hasattr(Product, key)]
        query = query.filter(and_(*filters))
    return query.first()