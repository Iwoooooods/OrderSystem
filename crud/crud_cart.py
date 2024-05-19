from typing import Union

from sqlalchemy.orm import Session
from loguru import logger

from model.base import Cart

def crud_add_cart(db:Session, cart: Cart) -> Union[None, Cart]:
    try:
        db.add(cart)
        db.commit()
        return cart
    except Exception:
        logger.info(Exception)
        db.rollback()
    return None

def crud_get_cart_by_user_id(db:Session, user_id:int) -> Union[Cart, None]:
    return db.query(Cart).filter(Cart.user_id == user_id).first()
