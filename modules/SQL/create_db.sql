-- Note: the database structure is set up to enable fastest possible 
-- query read speeds -- this is why customer and receipt ids are indexed, 
-- since we want to find first all receipts a customer owns, and all the 
-- items in a specific receipt as fast as possibloe

CREATE TABLE products(
    price INTEGER,
    unit_price INTEGER,
    unit_measure TEXT,
    name_on_receipt TEXT,
    name_on_website TEXT,
    link_to_product TEXT,
    image_link TEXT,
    category TEXT,
    item_description TEXT,
    PRIMARY KEY (price, name_on_receipt));

CREATE TABLE receipts(
    receipt_id INTEGER,
    cust_id INTEGER,
    date TEXT,
    PRIMARY KEY (receipt_id));

CREATE INDEX cst_index ON receipts(cust_id);





CREATE TABLE receipt_item(
    receipt_id INTEGER,
    price INTEGER,
    name_on_receipt TEXT,
    FOREIGN KEY (price,name_on_receipt) REFERENCES products(price,name_on_receipt)
    FOREIGN KEY (receipt_id) REFERENCES receipts(receipt_id)

);

CREATE INDEX receipt_index ON receipt_item(receipt_id);


