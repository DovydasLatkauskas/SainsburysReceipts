from modules.product_search import GoogleProductSearch
from product_samples import *
import json
from config import SERPAPI_AUTH


def test_search_item():
    st = GoogleProductSearch(SERPAPI_AUTH)
    st.find_item(product1)
    
def test_get_links():
    
    st = GoogleProductSearch(SERPAPI_AUTH)
    st.response = json.load(open("tests/product1_serp.json", "r"))
    l,i = st.get_links()
    
    
    