from sqlalchemy.orm import Session
from sqlalchemy import and_
from typing import Union
from loguru import logger

from model.base import Product

def crud_get_multi_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(Product)
    if condition:
        filters = [getattr(Product, key) == value for key, value in condition.items() if hasattr(Product, key)]
        rows = query.filter(and_(*filters)).all()
    else:
        rows = query.all()
    return rows

def crud_get_one_by_condition(db: Session, condition: Union[dict, None] = None):
    print(f'get by: {condition}')
    query = db.query(Product)
    if condition:
        filters = [getattr(Product, key) == value for key, value in condition.items() if hasattr(Product, key)]
        query = query.filter(and_(*filters))
    return query.first()

def crud_get_product_by_id(db: Session, id: id):
    logger.info(f"Show detail of Product_{id}")
    query = db.query(Product)
    product = query.filter(Product.id == id).first()
    return product