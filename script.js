async function getReceipts() {
    return [
        {
            receipt_id: 123,
            line_items: [
                {
                    name: "Waitrose Essential Oatmilk",
                    price: 1.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/4/LN_718674_BP_4.jpg",
                },
                {
                    name: "Oat Milk Hot Chocolate",
                    price: 2.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/11/LN_595718_BP_11.jpg",
                },
            ],
        },
        {
            receipt_id: 123,
            line_items: [
                {
                    name: "Oat Milk Hot Chocolate",
                    price: 2.99,
                    quantity: 1,
                    image_url: "https://ecom-su-static-prod.wtrecom.com/images/products/11/LN_595718_BP_11.jpg",
                },
            ],
        },
        {
            receipt_id: 456,
            line_items: [
                {
                    name: "Milk",
                    price: 2.49,
                    quantity: 2,
                    image_url: "https://assets.sainsburys-groceries.co.uk/gol/1137637/1/640x640.jpg",
                },
            ],
        },
        {
            receipt_id: 456,
            line_items: [
                {
                    name: "Milk",
                    price: 2.49,
                    quantity: 1,
                    image_url: "https://assets.sainsburys-groceries.co.uk/gol/1137637/1/640x640.jpg",
                },
            ],
        },
    ];
}
