## Introduction
This is a Django web application that displays a list of fruits and allows you to "purchase" fruits from it. 

## What's inside
* views.py - The views of the Django framework (MVT template)  
* home.html - Simple HTML template that allows interaction with the user through a browser
* url.py - Links the views.py and home.html together

## How it works
* The Django application is a full stack with postgreSQL being used as a database.
* The database has a products table that contains 3 columns named title, inventory_count and price.
* The home.html displays the contents of the products table and allows the user to sort by by all products and available products.
* If the user purchases a product, the value is decremented by one and the web page is refreshed. 
* Once there is no inventory left of the product, it will become unpurchusable. 
