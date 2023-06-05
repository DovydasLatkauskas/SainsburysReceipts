import sqlite3
from modules.Receipt import Receipt
from modules.Product import Product

def sql_query(f: str):
    with open(f,'r') as a:        
        return a.read()


class DbHandler():
    
    def __init__(self) -> None:
        self.conn = sqlite3.connect('sainsburys_v2.db')
        self.cursor = self.conn.cursor()
       
    def insert_receipt(self,cust_id,receipt:Receipt) -> tuple:
        '''inserts a receipt entry into database and returns inserted tuple'''
        self.cursor.execute(sql_query("modules/SQL/insert_receipt.sql"),
                            (cust_id,receipt.date))
        return self.cursor.fetchone()
    
    def insert_product(self,product:Product):
        self.cursor.execute(sql_query("modules/SQL/insert_product.sql"),
                            product.to_json())
    
    def insert_receipt_product_relation(self,product:Product,receipt_id):        
        self.cursor.execute(sql_query("modules/SQL/insert_receipt_item.sql"),
                            (receipt_id,product.price,product.name_on_receipt))
        
    def get_history(self, cust_id):
        receipts= self.__get_rids(cust_id)
        try:
            receipt_ids= [i[0] for i in receipts]
            dates = [i[2] for i in receipts]
        except:
            return []
        
        output = []
        print(receipts)
        for rid,d in zip(receipt_ids,dates):
            self.cursor.execute(sql_query("modules/SQL/get_history.sql"), (cust_id,rid))
            tuples = self.cursor.fetchall()
            colnames = self.cursor.description
            
            lineitems = [{k[0]:v for k,v in zip(colnames,i)} for i in tuples]
            receipt_dict = {'line_items':lineitems,'id':rid,'date':d}
            output.append(receipt_dict)
            
            
        return output

    def __get_rids(self, cid):
        self.cursor.execute(f"SELECT * FROM receipts where cust_id = {cid}")
        return self.cursor.fetchall()  
    
    def commit_and_close(self):
        self.conn.commit()
        self.conn.close()
    
    
    
    