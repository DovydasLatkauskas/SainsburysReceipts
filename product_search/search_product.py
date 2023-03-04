import json
from product_search.models.Product import Product
from serpapi import GoogleSearch
from private_api_key import private_api_key

def search_product(input_product : Product):
    link = get_product_link(input_product)
    input_product.populate_product_using_link(link)
    return input_product

def get_product_link(input_product : Product):
    name_on_receipt = input_product.name_on_receipt

    # returns [pounds, pence] in int

    search_query : str = f"{name_on_receipt} £{input_product.price} Sainsbury's"
    # e.g. "cocoa powder £3.15 site:https://www.sainsburys.co.uk/"


    params = {
    "q": search_query,
    "hl": "en",
    "gl": "uk",
    "google_domain": "google.com",
    "api_key": private_api_key
    }

    search = GoogleSearch(params)

    results = search.get_dict()
    link = __get_link_from_results(results)
    image_link = __get_inline_image_link(results)
    return link, image_link

def __get_inline_image_link(results):
    return results["inline_images"][0]["original"]
    
def __populate_product_using_link(input_product : Product, link : str):
    pass

def __get_link_from_results(results):
    return results["organic_results"][0]["link"]

def __pounds_to_pence(price_in_pence: int):
    pounds = price_in_pence // 100
    pence = price_in_pence % 100
    return [pounds, pence]
