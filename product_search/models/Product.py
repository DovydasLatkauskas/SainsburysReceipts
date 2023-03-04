from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import json
import re

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
    
    def populate_product_using_link(self, link, imlink):
        """done by martina, populates product object with data from Sainsbury's website"""
        #def fix_url(url):
        new_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F'
        ending_index = link.rfind('/')
            #print(ending_index)
            #new_url = new_url + url[ending_index+1:]
            #print(new_url)
        new_url = new_url + link[ending_index+1:]

        
        def scrape_url(link):
            page = requests.get(new_url)
            html = page.content
            soup = BeautifulSoup(html, 'html.parser')
            json_site = json.loads(soup.text)
            
            return json_site
        
        json_site = scrape_url(link)
        if json_site['errors']:
            #print(imlink)
            r = re.search(r"\/(\d+)\/", imlink)
            r = r.group(0)
           # print('r', r)
            new_url = new_url + '-' + r[1:-1] + '-p'
            #print(new_url)
            scrape_url(new_url)
            
       # print(json_site)
        category = json_site['products'][0]["breadcrumbs"][0]["label"]
        name_on_website = json_site['products'][0]['name']
        image_link = json_site['products'][0]['image']

#c = Product(0.6, 'hello')
#print(c.category)
