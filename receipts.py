from veryfi import Client
from abc import ABC
import json

class VerifyParser():
    def __init__(self,filename: str) -> None:
        self.client_id = 'vrfB0juUkBA4LwC5vwGrBUhwboiuwIMPRU68LTB'
        self.client_secret = '3Dnhw0PwbAkX3gtJa3iAJHuxKGsYUU1cgAE4y6e5cjyaUsvhyjUJuJOWoaccKTPH8jxyiVSTh7JkrPefMlz3Ac70u0oY3POTRyozlCbaNSAydG6ZN1UU2G7wHtwNkWzc'
        self.username = 'marlycef4'
        self.api_key = '98e6a79ff2bd95c85d82b5d2c2229ef6'
        self.categories = ['Grocery', 'Utilities', 'Travel']
        self.file_path = filename
        self.items = None
        self.response = None



    def get_response(self) -> None:
        veryfi_client = Client(self.client_id, 
                                self.client_secret, 
                                self.username, 
                                self.api_key)
        
        response = veryfi_client.process_document(self.file_path, 
                                                    categories=self.categories)
        self.response = response
        self.items = response["line_items"]

    def get_date(self) -> str:
        if self.items == None:
            self.get_response()
        
        return self.response["created_date"]
    
    def get_line_items(self):
        pass




parser = VerifyParser('bad receipt.jpg')
date = parser.get_date()
print(date)

print(parser.response)