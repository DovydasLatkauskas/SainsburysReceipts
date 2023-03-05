import requests
import sqlite3
import json

url = "http://127.0.0.1:8000"

def test_submission_to_db():
    '''test receipt submission to database'''

    api_call = "/api/submit_receipt"
    data = json.dumps({"date":"2023-02-27 22:20:53","line_items":
            [{"name":"LINDT INTENSE ORANG","price":1.60},
            {"name":"OATLEY BARISTA","price":2.40}]
            })
    
    data = json.dumps({"date":"2023-03-05 05:57:27","line_items":[{"name":"CK VERY CHERRY","price":2.5},{"name":"JS CUCUMBER WHOLE","price":0.8},{"name":"LINDT EXCEL MILK","price":1.6},{"name":"JS BRAEBURN X4","price":1.5},{"name":"RWSE SQZY HON 340G","price":2.0},{"name":"KELL FRT N FIB 375G","price":2.3},{"name":"OATLEY BARISTA","price":2.4}]})
    headers = {'Content-type': 'Application/json'}

    response = requests.post(url=url+api_call,headers=headers, data=data)

    print(response,response.text)

    conn = sqlite3.connect('sainsburys.db')
    cursor = conn.cursor()

    command = """SELECT * FROM products"""
    cursor.execute(command)
    print(cursor.fetchall())
    print("\n")

    command = """SELECT * FROM receipts"""
    cursor.execute(command)
    print(cursor.fetchall())

    conn.close()

def test_history():
    '''test fetching history'''
    api_call = "/api/history"
    response = requests.get(url=url+api_call)

    print(response,response.text)

def test_dashboard():
    '''test fetching dashboard info'''
    api_call = "/api/dashboard"
    response = requests.get(url=url+api_call)

    print(response,response.text)

def test_receipt_parser():
    api_call = "/api/uploadfile"
    files = {'my_file': open('DSC_0065.JPG', 'rb')}
    print(files)
    res = requests.post(url+api_call, files=files)

    print(res.text) 


# test_receipt_parser()
# test_submission_to_db()

test_dashboard()