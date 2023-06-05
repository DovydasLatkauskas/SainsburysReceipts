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
        
        
    def get_links(self):
        def recursive_search(i:int = 0):
            link = self.response["organic_results"][i]["link"]
            if "product" in link:
                return i
            else:
                try:
                    recursive_search(i+1)
                except IndexError as e:
                    return 0
                
        i = recursive_search()
        link = self.response["organic_results"][i]["link"]
        
        try:
            image_link = self.response["inline_images"][i]["original"]
        except:
            image_link = ""

        return link,image_link
    
    