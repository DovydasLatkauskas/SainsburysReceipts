from product_search.models import GoogleProductSearch, Product
from product_search.search_product import *

def __lot_to_lop(list_of_tuples):
    output = list()
    for product_tuple in list_of_tuples:
        output.append(Product(product_tuple[1], product_tuple[0]))
    return output

private_api_key = "dda4738939d0f2e81f9a8c9f3d62d63cd429b0edee27241b4222c53380d82931"

list_of_tuples = [('IRN BRU 1L', 1.1), ('LINDT INTENSE ORANG', 1.6), ('LINDT INTENSE ORANG', 1.6), ('CARROTS LOOSE', 0.07)]

products = __lot_to_lop(list_of_tuples)
product = products[1]

new_product = get_product_link(product)
print(new_product)


'''
search_tool = GoogleProductSearch.GoogleProductSearch(product)
search_tool.do_search()

print("saving response to file")
with open("test_serpAPI.txt","w") as f:
    json.dump(search_tool.response,f)

link = search_tool.get_first_result_link()

print(link)

'''