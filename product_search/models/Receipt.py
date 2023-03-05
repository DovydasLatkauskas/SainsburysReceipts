from typing import List
from product_search.models.Product import Product
from dataclasses import dataclass
import uuid

@dataclass
class Receipt:
    products : List[Product]
    date : str
    id : int = (uuid.uuid4().int>>96) # should be created by the database

    def get_products(self):
        return self.products
    
    def get_date(self):
        return self.date