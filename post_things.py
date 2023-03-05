import requests


with open("DSC_0058.JPG",'rb') as f:
    image = f.read()
file = {"file":image}
print(file)
domain = "http://127.0.0.1:8000"
dir = "/api/raw_receipt"
response = requests.post(domain+dir,data=file)