
from sqlalchemy.orm import Session

from crud.crud_product import crud_get_multi_by_condition, crud_get_one_by_condition, crud_get_product_by_id
from crud.crud_cart import crud_add_to_cart
from schema.product_schema import ProductQuery
from model.base import Cart

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

    async def add_to_cart(self, user_id, product_id: int, db: Session):
        cart = Cart(user_id=user_id, product_id=product_id)
        crud_add_to_cart(db, cart)

product_service = ProductService()