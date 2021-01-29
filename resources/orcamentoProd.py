from flask_restful import Resource, reqparse

from models.orcamentoProd import getByCodorc

class OrcamentoProd(Resource):
    args = reqparse.RequestParser()
    args.add_argument('query', type=str, required=True, help="The field name cant be empty")
    
    def get(self):
        data = OrcamentoProd.args.parse_args()
        
        try:
            products = getByCodorc(data['query'])
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500
        
        return products, 200
    
        