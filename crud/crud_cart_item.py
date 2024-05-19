from typing import List, Union

from sqlalchemy import and_
from sqlalchemy.orm import Session
from loguru import logger

from model.base import CartItem
from crud.crud_product import crud_get_product_by_id

def crud_add_cart_item(db: Session, product_id, cart_id, quantity) -> Union[CartItem, None]:
    try:
        price = crud_get_product_by_id(db, product_id).price
        cart_item = CartItem(product_id=product_id, cart_id=cart_id, quantity=quantity, price_at_time=price)
        db.add(cart_item)
        db.commit()
        return cart_item
    except Exception as e:
        db.rollback()
    return None

def crud_get_items_by_cart(db: Session, cart_id) -> Union[List[CartItem], None]:
    query = db.query(CartItem).filter(CartItem.cart_id == cart_id)
    return query.all()

def crud_get_item(db:Session, cart_id, product_id) -> Union[CartItem, None]:
    query = db.query(CartItem).filter(and_(CartItem.cart_id==cart_id, CartItem.product_id==product_id))
    return query.first()

def crud_update_cart_item(db: Session, product_id, cart_id, quantity) -> Union[CartItem, None]:
    condition = {
                'product_id': product_id,
                 'quantity': quantity,
                 'cart_id': cart_id
                 }
    try:
        price = crud_get_product_by_id(db, product_id).price
        cart_item = CartItem(price_at_time=price, **condition)
        db.query(CartItem).filter(and_(CartItem.cart_id==cart_id, CartItem.product_id==product_id)).update(condition)
        db.commit()
        return cart_item
    except Exception as e:
        db.rollback()
        logger.error(e)
    return None