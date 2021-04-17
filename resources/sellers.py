from flask_restful import Resource, reqparse

from models.sellers import getAllSellers


class Sellers(Resource):
    args = reqparse.RequestParser()

    def get(self):

        try:
            sellers = getAllSellers()
        except Exception as e:
            return {'message': 'Erro ao pesquisar o produto', 'error': str(e)}, 500

        return sellers, 200
