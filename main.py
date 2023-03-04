from fastapi import FastAPI
from test_main import image_to_list_of_tuples
from test_main import image_to_date
from test_main import lod_to_lop
from private_api_key import private_api_key
from product_search.models.Product import Product
from product_search.models.Receipt import Receipt
from pydantic import BaseModel
import sqlite3

def tuples_to_json(tuples):
    json_list = []
    for item in tuples:
        json_list.append({"name":item[0],"price":item[1]})
    
    return json_list

app = FastAPI()

conn = sqlite3.connect('sainsburys.db')
cursor = conn.cursor()

print("Opened database successfully")

cursor.execute("""CREATE TABLE IF NOT EXISTS receipts (
    id INTEGER PRIMARY KEY,
    date TEXT
    );""")

# check whether table PROJECTS exists, if not, create it
cursor.execute("""CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY ,
    price INTEGER,
    name_on_receipt TEXT,
    name_on_website TEXT,
    link_to_product TEXT,
    image_link TEXT,
    category TEXT,
    receipts_id INTEGER,
    FOREIGN KEY (receipts_id) REFERENCES receipts (id)
    );""")



@app.get("/")
async def root():
    return {"message": "Hello World"}

class JSON_OBJECT(BaseModel):
    date: str
    line_items: list

@app.post("/api/raw_receipt")
async def scan_receipt(image):
    list_of_tuples = image_to_list_of_tuples(image)
    json_list = tuples_to_json(list_of_tuples)
    date = image_to_date(image)
    json = {"date":date,"line_items":json_list}
    return json

'''
image = "DSC_0058.JPG"
list_of_tuples = image_to_list_of_tuples(image)
json_list = tuples_to_json(list_of_tuples)
print(json_list)
'''


@app.post("/api/submit_receipt")
async def add_receipt(json: JSON_OBJECT):
    #create a list of products from the list of product tuples from user
    line_items = json.line_items
    list_of_products = lod_to_lop(line_items)
    receipt = Receipt(products=list_of_products,date=json.date)
    add_to_database(receipt)






def add_to_database(receipt: Receipt):
    cursor.execute("""
    INSERT INTO receipts (id, date) VALUES (?, ?);
    """, (receipt.id, receipt.date))
    conn.commit()
    for product in receipt.products:
        cursor.execute("""
        INSERT INTO products (id, price, name_on_receipt, name_on_website, link_to_product, image_link, category, receipts_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (product.id, product.price, product.name_on_receipt, product.name_on_website, product.link_to_product, product.image_link, product.category, receipt.id))
        conn.commit()