from fastapi import FastAPI
from test_main import image_to_list_of_tuples
from test_main import image_to_date
from test_main import lod_to_lop
from private_api_key import private_api_key
from product_search.models.Product import Product
from product_search.models.Receipt import Receipt
from pydantic import BaseModel
from fastapi import File, UploadFile
import sqlite3
import aiofiles
import numpy as np
import random
import os
from fastapi.middleware.cors import CORSMiddleware
import time

def tuples_to_json(tuples):
    json_list = []
    for item in tuples:
        json_list.append({"name":item[0],"price":item[1]})
    
    return json_list

app = FastAPI()

#fix problems with cors
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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

 
class JSON_OBJECT(BaseModel):
    date: str
    line_items: list


@app.post("/api/uploadfile")
async def scan_receipt(my_file: UploadFile = File(...)):
    print("something happened")
    img = await my_file.read()

    #create a temporary image file
    async with aiofiles.open("destination.jpg" , "wb") as f:
        await f.write(img)

    image = "destination.jpg"

    #parse the data in the image
    print("creating list of tuples; parsing receipt via veryfiAPI")
    #list_of_tuples = image_to_list_of_tuples(image)
    print("creating json")
    #json_list = tuples_to_json(list_of_tuples)
    #date = image_to_date(image)
    time.sleep(2)

    #create json to be sent to frontend with basic receipt data 
    #json = {"date":date,"line_items":json_list}
    #print("returning json")
    return json


@app.post("/api/submit_receipt")
async def add_receipt(json: JSON_OBJECT):
    """submit the processed receipt data to the database"""
    
    #create a list of products from the list of product tuples from user
    #this includes parsin SB's website
    print(json.line_items)
    list_of_products = lod_to_lop(json.line_items)
    print(list_of_products)
    receipt = Receipt(products=list_of_products,date=json.date)
    add_to_database(receipt)


@app.get("/api/history")
async def fetch_shopping_history():
    #json file that will contain purchase history; this will get returnned
    json_file = []

    #connect to database
    conn = sqlite3.connect('sainsburys.db')
    cursor = conn.cursor()

    #get ids for each receipt
    command = """SELECT id FROM receipts"""
    cursor.execute(command)
    receipt_ids = cursor.fetchall()


    for id in receipt_ids:
        individual_receipt = {}
        individual_receipt["receipt_id"] = id[0]
        individual_receipt_line_items = []

        print(id)


        #select all line items (products) from receipt with specific id
        command = f"""SELECT * FROM products WHERE receipts_id = '{id[0]}'"""
        cursor.execute(command)
        line_items = cursor.fetchall()
        print(line_items)

        for tuple_item in line_items:
            item = {}
            item["id"] = tuple_item[0]
            item["price"] = tuple_item[1]
            item["name_on_receipt"] = tuple_item[2]
            item["name_on_website"] = tuple_item[3]
            item["link_to_product"] = tuple_item[4]
            item["image_link"] = tuple_item[5]
            item["category"] = tuple_item[6]
            item["receipt_id"] = id
            individual_receipt_line_items.append(item)
        
        individual_receipt["line_item"] = individual_receipt_line_items

        json_file.append(individual_receipt)

    return json_file
        

@app.get("/api/dashboard")
async def fetch_dashboard_data():
    conn = sqlite3.connect('sainsburys.db')
    cursor = conn.cursor()

    username = "Bob"
    nectar_points = 1345

    def expenses():
        command = """SELECT price FROM products"""
        cursor.execute(command)
        prices = cursor.fetchall()
        expenses = np.sum(prices)

        return expenses
    
    def categories():
        command = """SELECT category FROM products"""
        cursor.execute(command)
        categories = cursor.fetchall()

        category_data = {}
        unique, counts = np.unique(categories, return_counts = True)
        for i,j in zip(unique,counts):
            print(i,type(i))
            #calculate % for each category
            category_data[i] = float(j) / np.sum(counts) *100

        return category_data

    return {
        "username":username,
        "nectar_points":nectar_points,
        "expenses":expenses(),
        "category_data":categories()}


@app.post("/api/uploadviajson")
async def scan_receipt(my_file: JSON_OBJECT):
    print("something happened")

    image_base64 = my_file.image
    imgdata = base64.b64decode(image_base64)

    with open("temp.jpg", 'wb') as f:
        f.write(imgdata)

    image = "temp.jpg"

    #parse the data in the image
    list_of_tuples = image_to_list_of_tuples(image)
    json_list = tuples_to_json(list_of_tuples)
    date = image_to_date(image)

    #create json to be sent to frontend with basic receipt data 
    json = {"date":date,"line_items":json_list}
    return json



    


'''
image = "DSC_0058.JPG"
list_of_tuples = image_to_list_of_tuples(image)
json_list = tuples_to_json(list_of_tuples)
print(json_list)

@app.post("/api/raw_receipt")
async def scan_receipt(image):
    list_of_tuples = image_to_list_of_tuples(image)
    json_list = tuples_to_json(list_of_tuples)
    date = image_to_date(image)
    json = {"date":date,"line_items":json_list}
    return json
'''






def add_to_database(receipt: Receipt):
    command = """
    INSERT INTO receipts (id, date)
    VALUES (?, ?)
    """
    data =  (receipt.id, receipt.date)
    print("insertable data: ", data)
    cursor.execute(command, data)
    print("Inserted successfully")
    conn.commit()
    for product in receipt.products:

        print("Inserting Products")
        cursor.execute("""
        INSERT INTO products (id, price, name_on_receipt, name_on_website, link_to_product, image_link, category, receipts_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """, (random.randint(0,1827), product.price, product.name_on_receipt, product.name_on_website, product.link_to_product, product.image_link, product.category, receipt.id))
        conn.commit()
