from dataclasses import dataclass
from typing import List

@dataclass
class MonthlyStatistics:
    #these all are provisional, suggestions welcome
    monthlySpending: float
    category_spending: list[tuple]
    category_targets: list[tuple]
    category_progress: list[tuple]
    nectar_points: int
    
    # blah blah blah

    def __init__(self, price, name_on_receipt): 
        self.price = price
        self.name_on_receipt = name_on_receipt
