import requests
from PIL import Image


with open("DSC_0058.JPG",'rb') as f:
    image = f.read()
file = {"file":image}

domain = "http://127.0.0.1:8000"
dir = "/api/raw_receipt"
response = requests.post(domain+dir,data=image)