
from sqlalchemy.orm import Session

from crud.crud_product import crud_get_multi_by_condition, crud_get_one_by_condition, crud_get_product_by_id
from crud.crud_cart import crud_add_cart, crud_get_cart_by_user_id
from crud.crud_cart_item import crud_add_cart_item, crud_get_items_by_cart, crud_get_item, crud_update_cart_item
from schema.product_schema import ProductQuery
from model.base import Cart, Product


class ProductService:
    async def get_home_product(self, api_in: ProductQuery, db: Session):
        condition = {}
        product_name, category, description = api_in.product_name, api_in.category, api_in.description

        if product_name:
            condition['product_name'] = product_name
        if category:
            condition['category'] = category
        if description:
            condition['description'] = description

        rows = crud_get_multi_by_condition(db, condition)
        rws_by_page = rows[api_in.page_size * (api_in.page_number - 1): api_in.page_size * api_in.page_number]
        return [row.to_dict() for row in rws_by_page]

    async def get_product_detail(self, id: int, db: Session):
        product = crud_get_product_by_id(db, id)
        return product.to_dict()

    async def add_or_update_cart(self, user_id, product_id, quantity, db: Session):
        cart = crud_get_cart_by_user_id(db, user_id)
        if cart:
            item = crud_get_item(db, cart.id, product_id)
            if item:
                crud_update_cart_item(db, product_id, cart.id, quantity)
        else:
            crud_add_cart_item(db, product_id, crud_add_cart(db, Cart(user_id=user_id)).id, quantity)

    async def show_cart(self, user_id: int, db: Session):
        cart = crud_get_cart_by_user_id(db, user_id)
        items = crud_get_items_by_cart(db, cart.id)
        return [item.to_dict() for item in items]



product_service = ProductService()