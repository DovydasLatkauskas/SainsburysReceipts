from serpapi import GoogleSearch
from models import Product, Receipt
from dataclasses import dataclass

@dataclass
class GoogleProductSearch():
    line_item: Product = line_item
    response = {}
    params = {}
        
    def do_search(self) -> None:
        if self.params == {}:
            self.__product_to_serpapi_json()
        """Perform the actrual Google search with serpAPI"""
        search = GoogleSearch()
        self.response = search.get_dict()

    def get_first_result_link(self) -> None:
        """Get the link to the first search result, which will be used later to get the json from sainsburys"""

        if self.response == {}:
            self.do_search()
        return self.response["organic_results"][0]["link"]
    
    def __product_to_serpapi_json(self) -> dict:
        """converts the product object to a json that will be used in the google search"""

        self.params = {
            "q": self.line_item.name_on_receipt,
                "hl": "en",
                "gl": "uk",
                "google_domain": "google.com",
                "api_key": private_api_key
        }

        return params
    
