# REST API using Flask

CONTENTS OF THIS FILE

---------------------

The Aim of this project is to create a REST API for an e-commerce website.

 * Introduction
 * Requirements
 * Installation
 * Working
 * Maintainers

 ----

# INTRODUCTION

The idea for the project was to provide a REST API for e-commerce websites that is easy to use and comprehend. There are 3 types of models that I developed while working on this project :
1. Product
2. User
3. Order

The different endpoints (methods) provided to perform operations are:
1. Create
2. Read
3. Update
4. Delete

# REQUIREMENTS

This module requires Python3 to be installed in your system.

1. To check if Python is installed in your system :

        python --version

    * Then you should see something like this :

          Python 3.9.1
    
    * If not installed, go to https://www.python.org/downloads/ 

2. Then verify if pip was installed successfully:

          pip -V

    * Then you should see something like this :

          pip 20.2.3 from c:\python39\lib\site-packages\pip (python 3.9)

* Last thing required is Postman, if not installed:
 -> Visit Here : https://www.postman.com/

# INSTALLATION

1. Install the REST API using Flask module by unzipping the folder or cloning the project in your 
system.

2. Install virtualenv using pip (if not already installed): 

        pip install virtualenv

3. Run the following command in the terminal :

        virtualenv env

    * Change the directory to the folder where you have cloned the repo and run :

          .\env\Scripts\activate

    * then you should see something like :

          (env) PS D:\python\


4. Install all dependencies by running the following command :

        pip install -r requirements.txt

5. Then to run the program run the following command in the terminal in the cloned repo :

        python app.py

6. To decativate the virtual environment and use your original Python environment, simply type ‘deactivate’ :

        deactivate

7. To create database :
 + switch to venv
 + type python for python console
 + then type in commands:
            
        from app import db

        db.create_all()

8. After that you can use Postman to send 
+ GET
+ POST
+ DELETE
+ PUT 
requests to work with the API

# WORKING

The API supports : 
* GET, POST, DELETE and PUT methods for both Products and Orders
* GET, POST, DELETE method sfor Users

## Products
This class stores 4 values:
1. ID (A product ID that is unique for every object)
2. Name (Name of the product)
3. Description (Description of the product)
4. Price (Price of the product)

> Endpoints

* To retrieve all the Products, send a GET request to : http://127.0.0.1:5000/products

* To retrieve a specific Product, send a GET request to : http://127.0.0.1:5000/products/id
(here replace id with the id of the object)

* To create a Product send a POST request to http://127.0.0.1:5000/products using Postman with raw JSON Data like :

        {
        "description": "Modern and stylish headphones",
        "name": "Boss Headphones",
        "price":900
        } 

* To update a Product send a PUT request to http://127.0.0.1:5000/products using Postman with raw JSON Data like :

        {
        "description": "Modern and stylish headphones with wireless Bluetooth connection",
        "name": "Boss Headphones",
        "price": 2000
        } 

* To delete a specific Product send a DELETE request to http://127.0.0.1:5000/products/id using Postman


## Users
This class stores 3 values:
1. ID (A user ID that is unique for every object)
2. Name (Name of the user)
3. Role (Customer/Retailer)

>Endpoints

* To retrieve all the Users, send a GET request to  : http://127.0.0.1:5000/users

* To retrieve a specific User, send a GET request to  : http://127.0.0.1:5000/user/id
(here replace id with the id of the object)

* To create a User send a POST request to http://127.0.0.1:5000/users using Postman with raw JSON Data like :

        {
        "username": "Devansh Singh",
        "role": "Customer"
        }

* To delete a specific User send a DELETE request to http://127.0.0.1:5000/users/id using Postman.

## Orders
This class stores 6 values:
1. ID (An order ID that is unique for every object)
2. Address (Address where order is to be delivered)
3. Order-Date (Date when the order is placed)
4. Order-Time (Time when the order is placed)
5. Username (Name of the user who placed the order)
6. Total-Price (Total price of the order placed)

> Endpoints

* To retrieve all the Orders, send a GET request to  : http://127.0.0.1:5000/orders

* To retrieve a specific Order, send a GET request to  : http://127.0.0.1:5000/orders/id
(here replace id with the id of the object)

* To create an Order send a POST request to http://127.0.0.1:5000/orders using Postman with raw JSON Data like :

        {
        "userID":3,
        "totalPrice":500,
        "address":"303, Swarn Apartments, Pitampura"
        }

* To update an Order send a PUT request to http://127.0.0.1:5000/orders using Postman with raw JSON Data like :

        {
        "userID":3,
        "totalPrice":1000,
        "address":"304, Swarn Apartments, Pitampura"
        }

* To delete a specific Order send a DELETE request to http://127.0.0.1:5000/orders/id using Postman.

MAINTAINERS
-----------

 * Devansh Singh :
   * [LinkedIn](https://www.linkedin.com/in/devnsh/)
   * [Mail](mailto:devanshsingh201001@gmail.com)
   * [GitHub](https://github.com/blaady-baldy)


        

