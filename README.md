# Sainsbury's Receipt Scanner & Purchase History

A program that lets you scan your sainsbury's receipts and view spending stats. Receipts are processed using an optical character recognition (OCR) API, and results are matched to entries in sainsburys.co.uk, providing more detailed information of the products in your purchase history. This enables you to e.g. see a detailed overview of your spending habits, including a breakdown of spending per category, and allows you to set spending goals as well.


## Sainsbury's Challenge

Our proposal is to integrate these features with the nectar card, so that customers can access a more detailed purchase history and have a better overview of their spending; purchases made when using the nectar card can automatically be added to a customer's purchase history, and any purchases made without the card can be added later with the receipt scanning feature.


## Usage

main.py contains the code for running the API used by the web interface. run main.py via uvicorn:

uvicorn main:app

to start the server. test_api.py can be used to run some simple tests on the api calls (parse receipt, populate database, retrieve purchase history from database etc.)


The web interface can be used to access the main dashboard with spending stats, as well as the purchase history. A pre populated database has been provided, along with some test images of receipts.