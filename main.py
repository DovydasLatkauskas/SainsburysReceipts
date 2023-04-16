from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from modules.Receipt import Receipt
from modules.parsers import VeryfiParser
from modules.product_search import GoogleProductSearch
from modules.DatabaseHandler import DbHandler

app = FastAPI()

#setup cors
origins = ["*"] #sayfdee

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JSON_OBJECT(BaseModel):
    '''defines the json object expected from frontend'''
    
    date: str
    line_items: list


@app.post("/api/uploadfile")
async def scan_receipt(my_file: UploadFile = File(...)):
    img = await my_file.read()
    
    parser = VeryfiParser()
    parser.process_image_bytes(img=img)
    basic_receipt = parser.create_receipt()
            
    return basic_receipt.to_json()


@app.post("/api/submit_receipt")
async def add_receipt(json: JSON_OBJECT):
    """submit the processed receipt data to the database"""
    
    receipt = Receipt()
    receipt.from_json(json)
    
    handler = DbHandler()
    inserted_tuple = handler.insert_receipt(receipt=receipt,cust_id=0)
    rid = inserted_tuple[0]
    
    for p in receipt.products:
        try:
            p.populate_product_via_db()
        except:
            search_tool = GoogleProductSearch()
            search_tool.find_item(p)
            p = search_tool.create_product()
            handler.insert_product(product=p)
            
            
        handler.insert_receipt_product_relation(receipt_id=rid,product=p)
        

@app.get("/api/history")
async def fetch_shopping_history():
    
    handler = DbHandler()
    hist = {"history":handler.get_history(cust_id=0)}
    
    return hist
        

@app.get("/api/dashboard")
async def fetch_dashboard_data():
    '''not yet implementeed'''
    
    return []

