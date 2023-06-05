from modules.parsers import VeryfiParser
from config import *

import pytest
import json

def test_create_valid_receipt():
    parser = VeryfiParser(VERYFI_AUTH)
    test_response = json.load(open("tests/valid_respose.json", "r"))
    parser.response = test_response
    test_receipt = parser.create_receipt()
    

def test_create_invalid_receipt():
    parser = VeryfiParser(VERYFI_AUTH)
    test_response = {}
    parser.response = test_response
    with pytest.raises(KeyError) as e:
        test_receipt = parser.create_receipt()
    


@pytest.mark.skip()
def test_process_file():
    parser = VeryfiParser(VERYFI_AUTH)
    parser.process_image_file("DSC_0058.JPG")
    
    
    
@pytest.mark.skip()
def test_process_bytes():
    parser = VeryfiParser(VERYFI_AUTH)
    with open("DSC_0058.JPG", "rb") as f:
        parser.process_image_bytes(f)
        