from dataclasses import dataclass

@dataclass
class Product:
    # instance variables
    id : int # should be created by the database??
    price : int
    name_on_receipt : str
    name_on_website : str
    image_link : str
    # category info?
    # nutritional info?

    # def __init__(self): # uncomment if we want to create an empty instance of Product
    #     pass

    def __init__(self, price, name_on_receipt): # data received from receipt
        self.price = price
        self.name_on_receipt = name_on_receipt

    # if we need getters and setters we can make them later
    # def get_price(self):
    #     return self.price
    
    # def set_price(self, new_price):
    #     self.price = new_price