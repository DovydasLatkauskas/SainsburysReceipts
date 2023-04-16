from dataclasses import dataclass
from typing import List
from Receipt import Receipt
from MonthlyStatistics import MonthlyStatistics

@dataclass
class User:
    # instance variables
    receipts: List[Receipt]
    monthlyStats: MonthlyStatistics

    # def __init__(self): # uncomment if we want to create an empty instance of Product
    #     pass

    def __init__(self): # data received from receipt
        # something
        return