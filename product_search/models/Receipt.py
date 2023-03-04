from Product import Product
import datetime
from dataclasses import dataclass

@dataclass
class Receipt:
    id : int # should be created by the database??
    products : [Product]
    datetime : datetime.datetime

    def __init__(self, products, datetime):
        self.products = products
        self.datetime = datetime

    def get_products(self):
        return self.products
    
    def get_datetime(self):
        return self.datetime