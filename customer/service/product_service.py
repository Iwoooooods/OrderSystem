
from sqlalchemy.orm import Session

from crud.crud_product import crud_get_multi_by_condition
from schema.page import MyPage

class ProductService:
    def get_home_product(self, api_in: MyPage, db: Session):
        crud_get_multi_by_condition(api_in, db)

product_service = ProductService()