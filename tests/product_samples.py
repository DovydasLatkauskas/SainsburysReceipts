from modules.Product  import Product
from modules.Receipt import Receipt


product1 = Product(
    price = 1.60,
    name_on_receipt = "LINDT INTENSE ORANG",
    name_on_website = 'Lindt Excellence Dark Orange Chocolate Bar 100g',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/large-bar-chocolate/lindt-excellence-intense-orange-100g',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/6294949/1/300x300.jpg',
    category = "Confectionery"
    )

product2 = Product(
    price = 1.10,
    name_on_receipt = "IRN BRU 1L",
    name_on_website = 'IRN-BRU Soft Drink 1L',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/irn-bru-1l-2417936-p',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/2417936/1/300x300.jpg',
    category = "Fruit flavoured"
    )

product3 = Product(
    price = 1.20,
    name_on_receipt = "IRN BRU 1L",
    name_on_website = 'IRN-BRU Soft Drink 1L',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/irn-bru-1l-2417936-p',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/2417936/1/300x300.jpg',
    category = "Fruit flavoured"
    )


receipt1 = Receipt(date="2023-02-27",products=[])

hist = [{'line_items': [{'price': 1.6, 'unit_price': 0, 'unit_measure': '', 'name_on_receipt': 'LINDT INTENSE ORANG', 'name_on_website': 'Lindt Excellence Dark Orange Chocolate Bar 100g', 'link_to_product': 'https://www.sainsburys.co.uk/gol-ui/product/large-bar-chocolate/lindt-excellence-intense-orange-100g', 'image_link': 'https://assets.sainsburys-groceries.co.uk/gol/6294949/1/300x300.jpg', 'category': 'Confectionery', 'item_description': ''}, {'price': 1.1, 'unit_price': 0, 'unit_measure': '', 'name_on_receipt': 'IRN BRU 1L', 'name_on_website': 'IRN-BRU Soft Drink 1L', 'link_to_product': 'https://www.sainsburys.co.uk/gol-ui/product/irn-bru-1l-2417936-p', 'image_link': 'https://assets.sainsburys-groceries.co.uk/gol/2417936/1/300x300.jpg', 'category': 'Fruit flavoured', 'item_description': ''}], 'id': 1, 'date': '2023-02-27'}]