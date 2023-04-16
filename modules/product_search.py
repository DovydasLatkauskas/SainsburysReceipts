import json
from modules.Product import Product
from serpapi import GoogleSearch
from modules.ApiToken import ApiToken

class GoogleProductSearch():
    
    def __init__(self,token: ApiToken) -> None:
        self.token = token
        self.response: any = None
    
    def find_item(self,item: Product):  
        search_query : str = f"{item.name_on_receipt} £{item.price} Sainsbury's"
        params = {
        "q": search_query,
        "hl": "en",
        "gl": "uk",
        "google_domain": "google.com",
        "api_key": self.token.api_key
        }

        self.response = GoogleSearch(params).get_dict()
        
        
    def create_product(self):
        link = ["organic_results"][0]["link"]
        
        try:
            image_link = self.response["inline_images"][0]["original"]
        except:
            image_link = ""
            
        p = Product(image_link=image_link)

        return p.populate_product_using_link(link)
    
    