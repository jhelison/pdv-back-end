from flask_restful import Resource, reqparse

from models.products import getByNameOrCode

class Products(Resource):
    args = reqparse.RequestParser()
    args.add_argument('query', type=str, required=True, help="The field name cant be empty")
    
    def get(self):
        data = Products.args.parse_args()
                                
        try:
            productsFinded = getByNameOrCode(data['query'])
        except Exception as e:
            return {'message': 'Erro ao pesquisar o produto', 'error': str(e)}, 500
        
        return productsFinded, 200