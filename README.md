# Sainsbury's Receipt Scanner & Purchase History

A program that lets you scan your sainsbury's receipts and view spending stats. Receipts are processed using an optical character recognition (OCR) API, and results are matched to entries in sainsburys.co.uk, providing more detailed information of the products in your purchase history. This enables you to e.g. see a detailed overview of your spending habits, including a breakdown of spending per category, and allows you to set spending goals as well. Matching items is done by searching the truncated item name on the receipt and item price using a google search API, and retrieving the first search result. 
# Sainsbury's Receipt Scanner & Purchase History

A program that lets you scan your sainsbury's receipts and view spending stats. Receipts are processed using an optical character recognition (OCR) API, and results are matched to entries in sainsburys.co.uk, providing more detailed information of the products in your purchase history. This enables you to e.g. see a detailed overview of your spending habits, including a breakdown of spending per category, and allows you to set spending goals as well. Matching items is done by searching the truncated item name on the receipt and item price using a google search API, and retrieving the first search result that matches from the Sainsbury's website.

## Sainsbury's Challenge

Our proposal is to integrate these features with the nectar card.

Nectar card holders could benefit from a more detailed overview of their spending habits with Sainsbury's, with a detailed purchase history and an easily accessible record of each item bought using nectar card, as well as a higher level breakdowns of their spending habits and the ability to set goals for e.g. spending less on sweets and more on fruits and vegetables.

Purchases made when using the nectar card can automatically be added to a customer's purchase history, and any purchases made without the card can be added later with the receipt scanning feature.


## Usage

**main.py** contains the code for running the API used by the web interface. run main.py via uvicorn:

> uvicorn main:app

to start the server. 

**test_api.py** can be used to run some simple tests on the api calls (parse receipt, populate database, retrieve purchase history from database etc.)


The web interface can be used to access the main dashboard with spending stats, as well as the purchase history. A pre populated database has been provided, along with some test images of receipts.