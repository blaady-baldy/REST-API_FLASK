from datetime import datetime, date
from enum import unique
from math import prod
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import false
app = Flask(__name__)

#-------------------------------------------------------------------------------------------------------------------------------
#                                             CONFIGURING THE FLASK APP

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "Home page for REST API"

#-------------------------------------------------------------------------------------------------------------------------------
#                                             MDOELS

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Integer, nullable = False)
    description = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.name} - {self.description} - {self.price}"

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    role = db.Column(db.String(80))

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address= db.Column(db.String(120), unique=True, nullable=False)
    totalPrice = db.Column(db.Integer, nullable = False)
    ordertime = db.Column(db.String(60))
    orderdate = db.Column(db.String(60))
    userID = db.Column(db.Integer, unique=True, nullable=False)

#-------------------------------------------------------------------------------------------------------------------------------
#                                                   ROUTES FOR PRODUCT

@app.route('/products')
def get_products():
    products = Product.query.all()
    output=[]
    for product in products:
        product_data = {'id':product.id,'price': product.price, 'name': product.name, 'description': product.description}
        output.append(product_data)
    return { "products" : output}

@app.route('/products/<id>')
def get_product(id):
    product = Product.query.get_or_404(id)
    return {"price": product.price, "name": product.name, "description": product.description}

@app.route('/products', methods=['POST'])
def create_product():
    product = Product(price=request.json['price'],
                    name=request.json['name'],
                  description=request.json['description'])
    db.session.add(product)
    db.session.commit()
    return {'id': product.id}

@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    if product is None:
        return {"error": "not found"}
    db.session.delete(product)
    db.session.commit()
    return {"message": "Deleted"}

@app.route('/products/<id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get(id)
    if product is None:
        return {"error": "not found"}
        
    product.price =request.json['price']
    product.name=request.json['name']
    product.description=request.json['description']

    db.session.add(product)
    db.session.commit()
    return {"message": "Updated"}

#-------------------------------------------------------------------------------------------------------------------------------
#                                                       ROUTES FOR USER

@app.route('/users')
def get_users():
    users = User.query.all()
    output=[]
    for user in users:
        user_data = {'id':user.id, 'name': user.username, 'role': user.role}
        output.append(user_data)
    return { "users" : output}

@app.route('/users/<id>')
def get_user(id):
    user = User.query.get_or_404(id)
    return {"id": user.id, "name": user.username, "role": user.role}

@app.route('/users', methods=['POST'])
def add_user():
    user = User(username=request.json['username'],
                  role=request.json['role'])
    db.session.add(user)
    db.session.commit()
    return {'id': user.id}

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)
    if user is None:
        return {"error": "not found"}
    db.session.delete(user)
    db.session.commit()
    return {"message": "DELETED"}

#-------------------------------------------------------------------------------------------------------------------------------
#                                                       ROUTES FOR ORDERS

@app.route('/orders')
def get_orders():
    orders = Order.query.all()
    output=[]
    for order in orders:
        userID = order.userID
        user = User.query.get_or_404(userID)
        userName = user.username
        
        order_data = {'id':order.id, 'username': userName, 'totalPrice:':order.totalPrice,
         'ordertime': order.ordertime, 'orderdate': order.orderdate, 'address':order.address}
        output.append(order_data)
    return { "orders" : output}

@app.route('/orders/<id>')
def get_order(id):
    order = Order.query.get_or_404(id)
    return {'id':order.id, 'userID': order.userID, 'totalPrice:':order.totalPrice,
         'ordertime': order.ordertime, 'orderdate': order.orderdate}

@app.route('/orders', methods=['POST'])
def add_order():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()

    order = Order(address=request.json['address'], userID=request.json['userID'],
    totalPrice=request.json['totalPrice'],
    ordertime=current_time, orderdate=current_date)

    db.session.add(order)
    db.session.commit()
    return {'id': order.id}

@app.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    order = Order.query.get(id)
    if order is None:
        return {"error": "not found"}
    db.session.delete(order)
    db.session.commit()
    return {"message": "DELETED"}

@app.route('/orders/<id>', methods=['PUT'])
def update_order(id):
    order = Order.query.get(id)
    if order is None:
        return {"error": "not found"}
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    current_date = date.today()

    order.totalPrice=request.json['totalPrice']
    order.userID=request.json['userID']
    order.address=request.json['address']
    order.ordertime=current_time
    order.orderdate=current_date
    

    db.session.add(order)
    db.session.commit()
    return {"message": "Updated"}
#-------------------------------------------------------------------------------------------------------------------------------
#                                                  RUNNING THE FLASK APP

if __name__=="__main__":
    app.run(debug=True)