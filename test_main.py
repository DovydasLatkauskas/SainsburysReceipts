
from product_search.models.Receipt import Receipt
from product_search.models.VeryfiParser import VeryfiParser
from product_search.search_product import search_product
from dataclasses import dataclass
import requests
from bs4 import BeautifulSoup
import json

@dataclass
class Product:
    # instance variables
    id : int = 0# should be created by the database??
    price : int = 0
    name_on_receipt : str = ''
    name_on_website : str = ''
    link_to_product : str = ''
    image_link : str = ''
    category : str = ""

    # nutritional info?

    # def __init__(self): # uncomment if we want to create an empty instance of Product
    #     pass



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
        
        json_link = fix_url(link)
        print(json_link)
        page = requests.get(json_link)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        json_site = json.loads(soup.text)
        print(json_site)
        self.category = json_site['products'][0]["breadcrumbs"][0]["label"]
        self.name_on_website = json_site['products'][0]['name']
        self.image_link = json_site['products'][0]['image']

@dataclass
class Receipt:
    id : int # should be created by the database??
    products : list[Product]
    datetime : str

    def __init__(self, products, datetime):
        self.products = products
        self.datetime = datetime

    def get_products(self):
        return self.products
    
    def get_datetime(self):
        return self.datetime 

def process_receipt(path_to_input_image):
    list_of_tuples = image_to_list_of_tuples(path_to_input_image)
    list_of_tuples = list_of_tuples[1:] #for testing purposes only; remove problematic irn bru for now
    list_of_products = lot_to_lop(list_of_tuples)
    date = image_to_date(path_to_input_image)
    receipt = Receipt(list_of_products, date)

    print("length of products:", len(receipt.products))
    
    # push Receipt object to database
    # database receipt object with id
    # push Receipt object to frontend with date converted to datetime

def image_to_list_of_tuples(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_line_items()

def image_to_date(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_date()

def lot_to_lop(list_of_tuples):
    output = list()
    for product_tuple in list_of_tuples:
        print(product_tuple)
        output.append(Product(name_on_receipt=product_tuple[0],price=product_tuple[1]))
    for product in output:
        product = search_product(product)
    return output

def lod_to_lop(list_of_dicts):
    output = list()
    for product in list_of_dicts:
        print(product)
        output.append(Product(name_on_receipt=product["name"],price=product["price"]))
    for product in output:
        product = search_product(product)
    return output

def __init__():
    image_path = "DSC_0058.JPG"
    process_receipt(path_to_input_image=image_path)