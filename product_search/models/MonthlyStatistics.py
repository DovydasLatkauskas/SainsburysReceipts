from dataclasses import dataclass
from typing import List

@dataclass
class MonthlyStatistics:
    monthlySpending: float
    # blah blah blah

    def __init__(self, price, name_on_receipt): 
        self.price = price
        self.name_on_receipt = name_on_receipt
