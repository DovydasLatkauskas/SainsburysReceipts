from dataclasses import dataclass
<<<<<<< Updated upstream
from typing import List
=======
from bs4 import BeautifulSoup
import requests
import json
>>>>>>> Stashed changes

@dataclass
class Product:
    # instance variables
<<<<<<< Updated upstream
    id : int # should be created by the database??
    price_in_pence : int
    name_on_receipt : str
    name_on_website : str
    link_to_product : str
    image_link : str
    category_levels: List[str]
    # category info?
=======
    id : int = 0# should be created by the database??
    price : int = 0
    name_on_receipt : str = ''
    name_on_website : str = ''
    link_to_product : str = ''
    image_link : str = ''
    category : str = ""
>>>>>>> Stashed changes
    # nutritional info?

    # def __init__(self): # uncomment if we want to create an empty instance of Product
    #     pass

<<<<<<< Updated upstream
    def __init__(self, price_in_pence, name_on_receipt): # data received from receipt
        self.price_in_pence = price_in_pence
        self.name_on_receipt = name_on_receipt
=======
>>>>>>> Stashed changes

    # if we need getters and setters we can make them later
    # def get_price(self):
    #     return self.price
    
    # def set_price(self, new_price):
    #     self.price = new_price
    
    def product_to_serpapi_json(self,private_api_key):
        """converts the product object to a json that will be used in the google search"""

        params = {
        "q": self.name_on_receipt,
            "hl": "en",
            "gl": "uk",
            "google_domain": "google.com",
            "api_key": private_api_key
        }
        
        return params
    
    def populate_product_using_link(self, link):
        """done by martina, populates product object with data from Sainsbury's website"""
        def fix_url(url):
            new_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F'
            ending_index = url.rfind('/')
            #print(ending_index)
            #new_url = new_url + url[ending_index+1:]
            #print(new_url)
            return new_url + url[ending_index+1:]

        page = requests.head(fix_url(link))
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        json_site = json.loads(soup.text)
        category = json_site['products'][0]["breadcrumbs"][0]["label"]
        name_on_website = json_site['products'][0]['name']
        image_link = json_site['products'][0]['image']

c = Product(0.6, 'hello')
print(c.category)
