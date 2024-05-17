from sqlalchemy.orm import Session
from loguru import logger

from model.base import Cart

def crud_add_to_cart(db:Session, cart: Cart):
    try:
        db.add(cart)
        db.commit()
    except Exception:
        logger.info(Exception)
        db.rollback()
