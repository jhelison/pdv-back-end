from flask import Flask, request
from flask_restful import Api
import random
from flask_jwt_extended import JWTManager
import os
import sqlalchemy.sql.default_comparator

from resources.products import Products
from resources.customer import Customer, Customers
from resources.orcamentoProd import OrcamentoProd
from resources.budget import Budget, Budgets
from resources.user import User, UserInfo, Users
from resources.sellers import Sellers

app = Flask(__name__)
# Database is installed on appdata/user/roaming
db_path = os.path.join(os.getenv('APPDATA'), 'CPlusAPP/')
db_uri = 'sqlite:///{}'.format(os.path.join(db_path, 'app.db'))
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MTExNzk0ODAsIm5iZiI6MTYxMTE3OTQ4MCwianRpIjoiZGYyOWU4ZTQtZWYzMS00Yjc3LWI4MjMtMTgyMWJlOWFlZjM3IiwiZXhwIjoxNjExMTgwMzgwLCJpZGVudGl0eSI6IjkxNGU5ZTUzNzcyMzBmYjciLCJmcmVzaCI6ZmFsc2UsInR5cGUiOiJhY2Nlc3MifQ.kNwqEZCMYVVh_6tjcboDShpa7Ih9BjZ40FuCk4WZowk'
api = Api(app)
jwt = JWTManager(app)


@app.before_first_request
def buildDatabase():
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    database.create_all()


@app.route('/')
def home():
    ip_address = request.remote_addr
    return f'<h1>Backend Running...{random.randint(1, 200)} {ip_address}:5000</h1>', 200


api.add_resource(Products, '/products/')
api.add_resource(Customer, '/customer/')
api.add_resource(Customers, '/customers/')
api.add_resource(Budgets, '/budgets/')
api.add_resource(Budget, '/budget')
api.add_resource(OrcamentoProd, '/orcamentoprod/')
api.add_resource(User, '/user/')
api.add_resource(Users, '/users')
api.add_resource(UserInfo, '/userinfo')
api.add_resource(Sellers, '/sellers')

if __name__ == '__main__':
    from sql_alchemy import database
    database.init_app(app)
    app.run(host='0.0.0.0', port=5000)
