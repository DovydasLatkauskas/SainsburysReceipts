from dataclasses import dataclass
import requests
import re

@dataclass
class Product:
    price : int = 0
    unit_price: int = 0
    unit_measure: str = ""
    name_on_receipt : str = ''
    name_on_website : str = ''
    link_to_product : str = ''
    image_link : str = ''
    category : str = ""
    item_description: str = ''

    
    def populate_product_using_link(self, link, imlink):
        new_url = 'https://www.sainsburys.co.uk/groceries-api/gol-services/product/v1/product?filter[product_seo_url]=gb%2Fgroceries%2F'
        ending_index = link.rfind('/')
        new_url = new_url + link[ending_index+1:]

        
        def scrape_url(link):
            page = requests.get(new_url)
            print(new_url,page.text)
            html = page.json()
            
            return html
        
        json_site = scrape_url(link)
       # print(json_site)
        try:
            json_site['errors']
            #print(imlink)
            r = re.search(r'\/(\d+)\/', imlink)
            r = r.group(0)
           # print('r', r)
            new_url = new_url + '-' + r[1:-1] + '-p'
            #print(new_url)
            json_site = scrape_url(new_url)
        except KeyError:
            json_site = scrape_url(link)
           
            
        self.name_on_website = json_site['products'][0]['name']
        self.image_link = json_site['products'][0]['image']
      
        try:
            self.category = json_site['products'][0]["breadcrumbs"][1]["label"]
        except:
          self.category = 'None'
    
    
    def to_json(self):
        return self.__dict__