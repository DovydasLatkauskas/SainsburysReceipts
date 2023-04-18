from modules.DatabaseHandler import DbHandler
from product_samples import *
import sqlite3
import pytest


def test_add_existing_products():
    db = DbHandler()
    print(product1.to_json())
    with pytest.raises(sqlite3.IntegrityError):
        db.insert_product(product=product1)
        db.insert_product(product=product2)
    
def test_add_new_products():
    db = DbHandler()
    db.insert_product(product=product3)
        
def  test_add_existing_receipt():
    db = DbHandler()
    db.insert_receipt(cust_id = 0, receipt = receipt1)
        
        
def test_history():
    db = DbHandler()
    h = db.get_history(cust_id=0)
    assert h == hist