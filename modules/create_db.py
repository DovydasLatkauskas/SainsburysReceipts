import sqlite3
from Receipt import Receipt
from Product import Product
from DatabaseHandler import DbHandler

def sql_query(f: str):
    with open(f,'r') as a:        
        return a.read()


def create_tables():
    conn = sqlite3.connect('sainsburys_v2.db')
    cursor = conn.cursor()


    cmds = sql_query("modules/SQL/create_db.sql").split(";")

    for c in cmds:
        print(c)
        cursor.execute(c)
product1 = Product(
    price = 1.60,
    name_on_receipt = "LINDT INTENSE ORANG",
    name_on_website = 'Lindt Excellence Dark Orange Chocolate Bar 100g',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/large-bar-chocolate/lindt-excellence-intense-orange-100g',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/6294949/1/300x300.jpg',
    category = "Confectionery"
    )

product2 = Product(
    price = 1.10,
    name_on_receipt = "IRN BRU 1L",
    name_on_website = 'IRN-BRU Soft Drink 1L',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/irn-bru-1l-2417936-p',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/2417936/1/300x300.jpg',
    category = "Fruit flavoured"
    )
def add_products():
        

    
    
    db = DbHandler()
    print(product1.to_json())
    db.insert_product(product=product1)
    db.insert_product(product=product2)
    db.commit_and_close()



    product_list = [product1,product2]

    receipt = Receipt(products = product_list, date= '2023-02-27 22:20:53')

def add_receipt():
    
    db = DbHandler()
    id = db.insert_receipt(cust_id = 0, receipt = Receipt(date="2023-02-27",products=[]))
    print(id)
    print("inser product1")
    db.insert_receipt_product_relation(receipt_id=id[0],product=product1)
    print("inser product2")
    db.insert_receipt_product_relation(receipt_id=id[0],product=product2)
    print("commit")
    db.commit_and_close()
    print("done")
    
    
# add_products()
add_receipt()