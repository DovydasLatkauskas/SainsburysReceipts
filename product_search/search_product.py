# from Receipt import Receipt
from Product import Product
from serpapi import GoogleSearch
from private_api_key import private_api_key

def search_product(input_product : Product):
    link = __get_product_link(input_product)
    __populate_product_using_link(input_product, link)
    return input_product

def __get_product_link(input_product : Product):
    name_on_receipt = input_product.name_on_receipt

    search_query : str = f"{name_on_receipt} site:https://www.sainsburys.co.uk/"

    params = {
    "q": search_query,
    "hl": "en",
    "gl": "uk",
    "google_domain": "google.com",
    "api_key": private_api_key
    }

    search = GoogleSearch(params)
    results = search.get_dict()

def __populate_product_using_link(input_product : Product, link : str):
    pass