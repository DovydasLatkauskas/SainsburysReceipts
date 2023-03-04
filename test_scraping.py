from product_search.models import Product


c = Product.Product(0.6, 'hello')
c.populate_product_using_link("https://www.sainsburys.co.uk/gol-ui/product/large-bar-chocolate/lindt-excellence-intense-orange-100g")
print(c.category, c.name_on_website)
