SELECT  products.price,
    products.unit_price,
    products.unit_measure,
    products.name_on_receipt,
    products.name_on_website,
    products.link_to_product,
    products.image_link,
    products.category,
    products.item_description


FROM receipts
LEFT JOIN receipt_item
ON receipts.receipt_id = receipt_item.receipt_id
LEFT JOIN products
on receipt_item.price = products.price and receipt_item.name_on_receipt = products.name_on_receipt
WHERE receipts.cust_id = ? and receipts.receipt_id = ?;