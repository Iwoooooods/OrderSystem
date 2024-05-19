from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    page_number: int = 1  # 页码
    page_size: int = 10  # 每页数量

class ProductQuery(ProductBase):
    product_name: Optional[str]
    category: Optional[str]
    description: Optional[str]

