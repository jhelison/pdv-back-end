from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import jwt_required, get_raw_jwt

from models.budget import addNewBudget

class Budget(Resource):
    args = reqparse.RequestParser()
    args.add_argument('data', type=str, required=True, help="The field data cant be empty")
    
    @jwt_required
    def post(self):
        data = Budget.args.parse_args()        
        
        try:
            codvend = get_raw_jwt()['identity']['codvend']
            addNewBudget(json.loads(data['data']), codvend)
        except Exception as e:
            return {'message': 'Erro ao acessar ao adicionar orçamento', 'error': str(e)}, 500
                
        return 400