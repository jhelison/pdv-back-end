from flask import Flask
from flask_restful import Api
import random
from flask_jwt_extended import JWTManager

from resources.products import Products
from resources.customers import Customers
from resources.customer import Customer
from resources.budgets import Budgets
from resources.orcamentoProd import OrcamentoProd
from resources.budget import Budget
from resources.user import User
from resources.sellers import Sellers
from resources.userInfo import UserInfo
from resources.topItems import TopItems

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTExNzk0ODAsIm5iZiI6MTYxMTE3OTQ4MCwianRpIjoiZGYyOWU4ZTQtZWYzMS00Yjc3LWI4MjMtMTgyMWJlOWFlZjM3IiwiZXhwIjoxNjExMTgwMzgwLCJpZGVudGl0eSI6IjkxNGU5ZTUzNzcyMzBmYjciLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.kNwqEZCMYVVh_6tjcboDShpa7Ih9BjZ40FuCk4WZowk'
api = Api(app)
jwt = JWTManager(app)

@app.before_first_request
def buildDatabase():
    database.create_all()

@app.route('/')
def home():
    return f'<h1>Backend Running...{random.randint(1, 200)}</h1>', 200

api.add_resource(Products, '/products/')
api.add_resource(Customer, '/customer/')
api.add_resource(Customers, '/customers/')
api.add_resource(Budgets, '/budgets/')
api.add_resource(Budget, '/budget')
api.add_resource(OrcamentoProd, '/orcamentoprod/')
api.add_resource(User, '/user/')
api.add_resource(UserInfo, '/userinfo')
api.add_resource(Sellers, '/sellers')
api.add_resource(TopItems, '/topitems')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(debug=True, host='10.0.0.103')
    