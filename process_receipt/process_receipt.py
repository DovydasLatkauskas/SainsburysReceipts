from product_search.models.Receipt import Receipt
from product_search.models.Product import Product
from product_search.models.VeryfiParser import VeryfiParser
from product_search.search_product import search_product

def process_receipt(path_to_input_image):
    list_of_tuples = __image_to_list_of_tuples(path_to_input_image)
    list_of_products = __lot_to_lop(list_of_tuples)
    date = __image_to_date(path_to_input_image)
    receipt = Receipt(list_of_products, date)

    return receipt
    
    # push Receipt object to database
    # database receipt object with id
    # push Receipt object to frontend with date converted to datetime

def __image_to_list_of_tuples(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_line_items()

def __image_to_date(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_date()

def __lot_to_lop(list_of_tuples):
    output = list()
    for product_tuple in list_of_tuples:
        output.append(Product(name_on_receipt=product_tuple[0],price=product_tuple[1]))
    for product in output:
        product = search_product(product)
    return output