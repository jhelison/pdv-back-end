from flask_restful import Resource, reqparse
from flask import request

from models.user import UserModel

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

class Dashboard(Resource):
    def get(self):
        try:
            users_count = UserModel.count_users()
        except Exception as e:
            print(e)

        return {
            "server_data": {
                "port": "5151",
                "acess_code": 20218759
            },
            "users_count": users_count,
            "users_active": 0
        }, 200
