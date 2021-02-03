from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_raw_jwt

from models.orcamentoProd import getByCodorc

class OrcamentoProd(Resource):
    args = reqparse.RequestParser()
    args.add_argument('query', type=str, required=True, help="The field name cant be empty")
    
    @jwt_required
    def get(self):
        data = OrcamentoProd.args.parse_args()
        
        try:
            flagAdmin = get_raw_jwt()['identity']['flagAdmin']
            products = getByCodorc(data['query'], flagAdmin)
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500
        
        return products, 200
    
        