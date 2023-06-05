from typing import List
from modules.Product import Product
from dataclasses import dataclass


@dataclass
class Receipt:
    products : List[Product]
    date : str