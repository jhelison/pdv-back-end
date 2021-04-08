from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import jwt_required, get_jwt

from models.budget import addNewBudget
from models.acess import AcessModel

class Budget(Resource):
    args = reqparse.RequestParser()
    args.add_argument('data', type=str, required=True, help="The field data cant be empty")
    
    @jwt_required
    def post(self):
        data = Budget.args.parse_args()    
        
        try:
            codvend = get_jwt()['identity']['codvend']
            acess = AcessModel(get_jwt()['identity']['userId'], 'budgetPOST')
            acess.saveAcess()
            addNewBudget(json.loads(data['data']), codvend)
        except Exception as e:
            return {'message': 'Erro ao acessar ao adicionar orçamento', 'error': str(e)}, 500
                
        return 400