def process_receipt(path_to_input_image):
    list_of_tuples = __image_to_list_of_tuples(path_to_input_image)
    list_of_products = __lot_to_lop(list_of_tuples)
    __populate_products(list_of_products)
    datetime = __image_to_datetime(path_to_input_image)
    receipt = Receipt(list_of_products, datetime)
    
    # push Receipt object to database
    # push Receipt object to frontend

def __image_to_list_of_tuples(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_line_items()

def __image_to_datetime(path_to_input_image):
    parser = VeryfiParser(path_to_input_image)
    return parser.get_date()

def __lot_to_lop(list_of_tuples):
    output = list()
    for product_tuple in list_of_tuples:
        output.append(Product(product_tuple[1], product_tuple[0]))
    return output

def __populate_products(list_of_products):
    for product in list_of_products:
        pass #TODO unfinished!