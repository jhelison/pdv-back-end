from flask_restful import Resource, reqparse

from models.customer import getByNameOrCode, checkIfUnique

class Customers(Resource):
    args = reqparse.RequestParser()
    args.add_argument('query', type=str, required=True, help="The field name cant be empty")
    
    def get(self):
        data = Customers.args.parse_args()
        
        try:
            customersFinded = getByNameOrCode(data['query'])
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500
        
        return customersFinded, 200
    