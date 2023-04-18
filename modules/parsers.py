from abc import ABC, abstractclassmethod
from modules.Receipt import Receipt
from modules.Product import Product
from modules.ApiToken import ApiToken
from veryfi import Client
import os
import io


class Parser(ABC):
    '''abstract class defining the structure of receipt parsers'''
    
    @abstractclassmethod
    def create_receipt(self) -> Receipt:
        '''returns a Receipt object'''    
        
    @abstractclassmethod
    def process_image_file(self,img: str) -> None:
        '''process an image file with name img'''
        
    @abstractclassmethod
    def process_image_bytes(self,img: bytes) -> None:
        '''process an image bytestring img'''
                


class VeryfiParser(Parser):
    def __init__(self, token:ApiToken) -> None:
        self.token = token
        self.response = None
        
    
    def process_image_file(self,img) -> None:
        veryfi_client = Client(self.token.client_id,
                               self.token.client_secret,
                               self.token.username,
                               self.token.api_key)
        
        response = veryfi_client.process_document(img,
                                                  categories=['Grocery'])
        self.response = response
            

    def process_image_bytes(self,img: bytes) -> None:
        name = ".tmp/"+str(hash(img)) + '.jpg'
        img = img.read()
        with open(name , "wb") as f:
            f.write(img)
            
            
        self.process_image_file(name)
        
        os.remove(name)


    def create_receipt(self) -> Receipt:
        items = list(map(lambda item: Product(name_on_receipt=item['description'], 
                                              price=item['total']), 
                         self.response["line_items"]))
        
        date = self.response["created_date"]
        
        return Receipt(products=items,date=date)
        
        