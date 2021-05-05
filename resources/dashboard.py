from flask_restful import Resource, reqparse
from flask import request

import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

class Dashboard(Resource):
    def get(self):
        return {
            "host": {
                "hostname": hostname,
                "IPAddr": IPAddr + ":5000"
            }
        }, 200
