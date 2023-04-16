from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests
import json
import re
import uuid

@dataclass
class Product:
    price : int = 0
    unit_price: int = 0
    unit_measure: str = ""
    name_on_receipt : str = ''
    name_on_website : str = ''
    link_to_product : str = ''
    image_link : str = ''
    category : str = ""
    item_description: str = ''

    
    def populate_product_using_link(self, link, imlink):
        new_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F'
        ending_index = link.rfind('/')
        new_url = new_url + link[ending_index+1:]

        
        def scrape_url(link):
            page = requests.get(new_url)
            html = page.content
            soup = BeautifulSoup(html, 'html.parser')
            json_site = json.loads(soup.text)
            
            return json_site
        
        json_site = scrape_url(link)
       # print(json_site)
        try:
            json_site['errors']
            #print(imlink)
            r = re.search(r'\/(\d+)\/', imlink)
            r = r.group(0)
           # print('r', r)
            new_url = new_url + '-' + r[1:-1] + '-p'
            #print(new_url)
            json_site = scrape_url(new_url)
        except KeyError:
            json_site = scrape_url(link)
           
            
        self.name_on_website = json_site['products'][0]['name']
        self.image_link = json_site['products'][0]['image']
        dairy_prod_list = ["Desserts", "Dairy & eggs", "World foods, kosher & halal", "Vegetarian, vegan & dairy free"]
        food_cup_list = ["Confectionery", "Rice, pasta & noodles", "Biscuits & crackers"]
      
     # categories to change : list("Fruit & vegetables", "Meat & fish", "Dairy, eggs & chilled", "Food cupboard")
        try:
          if json_site['products'][0]["breadcrumbs"][0]["label"] == "Fruit & vegetables":
              if json_site['products'][0]["breadcrumbs"][1]["label"] == "Fresh fruit":
                  self.category = json_site['products'][0]["breadcrumbs"][1]["label"] 
              else:
                  self.category = "Vegetables"
              
          elif json_site['products'][0]["breadcrumbs"][0]["label"] == "Meat & fish":
              if json_site['products'][0]["breadcrumbs"][1]["label"] == "Fish & seafood":
                  self.category = json_site['products'][0]["breadcrumbs"][1]["label"] 
              else:
                  self.category = "Meat"
              
          elif json_site['products'][0]["breadcrumbs"][0]["label"] == "Dairy, eggs & chilled":
              if json_site['products'][0]["breadcrumbs"][1]["label"] in dairy_prod_list:
                  self.category = json_site['products'][0]["breadcrumbs"][1]["label"] 
              else:
                  self.category = "Chilled and ready made"
                  
          
          elif json_site['products'][0]["breadcrumbs"][0]["label"] == "Food cupboard":
              if json_site['products'][0]["breadcrumbs"][1]["label"] in food_cup_list:
                  self.category = json_site['products'][0]["breadcrumbs"][1]["label"] 
              else:
                  self.category = "Food cupboard"
          else:
              self.category = json_site['products'][0]["breadcrumbs"][0]["label"]
        except IndexError:
          self.category = 'None'
    
    
    def to_json(self):
        return self.__dict__
c = Product(0.6, 'hello')
print(c.to_json())
