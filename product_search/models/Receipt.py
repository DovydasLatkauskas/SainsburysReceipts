from typing import List
from product_search.models.Product import Product
from dataclasses import dataclass

@dataclass
class Receipt:
    id : int # should be created by the database
    products : List[Product]
    date : str

    def __init__(self, products, datetime):
        self.products = products
        self.date = date

    def get_products(self):
        return self.products
    
    def get_date(self):
        return self.date