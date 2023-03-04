from dataclasses import dataclass

@dataclass
class Product:
    # instance variables
    id : int = 0# should be created by the database??
    price : int = 0
    name_on_receipt : str = ''
    name_on_website : str = ''
    link_to_product : str = ''
    image_link : str = ''
    category : str = ""

    # nutritional info?

    # def __init__(self): # uncomment if we want to create an empty instance of Product
    #     pass



    # if we need getters and setters we can make them later
    # def get_price(self):
    #     return self.price
    
    # def set_price(self, new_price):
    #     self.price = new_price
    
    def product_to_serpapi_json(self,private_api_key):
        """converts the product object to a json that will be used in the google search"""

        params = {
        "q": self.name_on_receipt,
            "hl": "en",
            "gl": "uk",
            "google_domain": "google.com",
            "api_key": private_api_key
        }
        
        return params
    
    def populate_product_using_link(self, link):
        """done by martina, populates product object with data from Sainsbury's website"""
        def fix_url(url):
            new_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F'
            ending_index = url.rfind('/')
            #print(ending_index)
            #new_url = new_url + url[ending_index+1:]
            #print(new_url)
            return new_url + url[ending_index+1:]
        
        json_link = fix_url(link)
        print(json_link)
        page = requests.get(json_link)
        html = page.content
        soup = BeautifulSoup(html, 'html.parser')
        json_site = json.loads(soup.text)
        print(json_site)
        self.category = json_site['products'][0]["breadcrumbs"][0]["label"]
        self.name_on_website = json_site['products'][0]['name']
        self.image_link = json_site['products'][0]['image']


@dataclass
class Receipt:
    id : int # should be created by the database??
    products : list[Product]
    datetime : str

    def get_products(self):
        return self.products
    
    def get_datetime(self):
        return self.datetime


product1 = Product(
    id = 0,
    price = 1.60,
    name_on_receipt = "LINDT INTENSE ORANG",
    name_on_website = 'Lindt Excellence Dark Orange Chocolate Bar 100g',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/large-bar-chocolate/lindt-excellence-intense-orange-100g',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/6294949/1/300x300.jpg',
    category = "Confectionery"
    )

product2 = Product(
    id = 1,
    price = 1.10,
    name_on_receipt = "IRN BRU 1L",
    name_on_website = 'IRN-BRU Soft Drink 1L',
    link_to_product = 'https://www.sainsburys.co.uk/gol-ui/product/irn-bru-1l-2417936-p',
    image_link = 'https://assets.sainsburys-groceries.co.uk/gol/2417936/1/300x300.jpg',
    category = "Fruit flavoured"
    )



product_list = [product1,product2]

receipt = Receipt(id = 3, products = product_list, datetime= '2023-02-27 22:20:53')

