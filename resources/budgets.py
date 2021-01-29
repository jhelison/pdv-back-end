from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import jwt_required, get_raw_jwt

from models.budgets import getAllBudgets

class Budgets(Resource):
    args = reqparse.RequestParser()
    args.add_argument('page', type=int, required=True, help="The field page cant be empty")
    args.add_argument('filters', required=False, help="The filters page cant be empty")
    
    @jwt_required
    def get(self):
        data = Budgets.args.parse_args()
        filters = json.loads(data['filters'])
                
        try:
            codvend = get_raw_jwt()['identity']['codvend']
            budgetsList = getAllBudgets(data['page'], filters, codvend)
        except Exception as e:
            print(e)
            return {'message': 'Erro ao acessar a lista de orçamentos', 'error': str(e)}, 500
                
        return budgetsList, 200