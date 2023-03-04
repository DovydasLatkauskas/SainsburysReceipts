from fastapi import FastAPI
from product_search.models.Product import Product
from product_search.models.Receipt import Receipt
import sqlite3

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

@app.post("/api/raw_receipt")
async def scan_receipt(image):
    list_of_tuples = __image_to_list_of_tuples(image)
    date = __image_to_date(image)
    return list_of_tuples, date

@app.post("/api/submit_receipt")
async def add_receipt(list_of_correct_tuples,date):
    #create a list of products from the list of product tuples from user
    list_of_products = __lot_to_lop(list_of_correct_tuples)
    receipt = Receipt(products=list_of_products,datetime=date)
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