from product_search.models import VeryfiParser
import json

file = "DSC_0058.JPG"
parser = VeryfiParser.VeryfiParser(file)

items = parser.get_line_items()
print(items)

with open(file+".csv","w") as f:
    json.dump(items,f)