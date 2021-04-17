from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt

from models.products import getByNameOrCode


class Products(Resource):
    args = reqparse.RequestParser()
    args.add_argument('query', type=str, required=True,
                      help="The field name cant be empty")

    @jwt_required()
    def get(self):
        data = Products.args.parse_args()

        try:
            flagAdmin = get_jwt()['identity']['flagAdmin']
            productsFinded = getByNameOrCode(data['query'], flagAdmin)
        except Exception as e:
            return {'message': 'Erro ao pesquisar o produto', 'error': str(e)}, 500

        return productsFinded, 200
