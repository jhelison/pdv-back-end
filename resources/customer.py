from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import jwt_required, get_raw_jwt

from models.customer import getByNameOrCode, checkIfUnique, getNextCod, insertNewCustomer, updateCustomer, getByCode, getByName
from models.acess import AcessModel

class Customer(Resource):
    args = reqparse.RequestParser()
    args.add_argument('data', type=str, required=False, help="The field data cant be empty")
    args.add_argument('query', type=str, required=False, help="The field name cant be empty")
    
    def get(self):
        data = Customer.args.parse_args()
        
        try:
            customer = getByCode(data['query'])
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500
        
        return customer, 200
    
    @jwt_required
    def put(self):
        data = json.loads(Customer.args.parse_args().data)
                        
        try:
            acess = AcessModel(get_raw_jwt()['identity']['userId'], 'customerPUT')
            acess.saveAcess()
            isUnique, field = checkIfUnique(data)
        except Exception as e:
            return {'message': 'Erro na tentativa de cadastro', 'error': str(e)}, 500
        
        if(not isUnique):
            if field:
                return {'message': 'Cliente já cadastrado', 'error': f'Campo {field} já existente', 'data': field}, 409
            return {'message': 'Cliente vazio', 'error': f'Campo NOMECLI vazio', 'data': field}, 409
        
        try:
            newCode = getNextCod()
            newCustomer = {**data, **newCode}
            insertNewCustomer(newCustomer)
        except Exception as e:
            return {'message': 'Erro na tentativa de cadastro', 'error': str(e)}, 500
        
        try:
            return {'message': 'Cliente cadastrado com sucesso!', 'data': getByName(data['NOMECLI'])}, 200
        except Exception as e:
            return {'message': 'Erro na tentativa de cadastro', 'error': str(e)}, 500
    
    @jwt_required
    def post(self):
        data = json.loads(Customer.args.parse_args().data)
                
        try:
            acess = AcessModel(get_raw_jwt()['identity']['userId'], 'customerPOST')
            acess.saveAcess()
            updateCustomer(data)
        except Exception as e:
            return {'message': 'Erro na tentativa de atualização', 'error': str(e)}, 500
                
        try:
            return {'message': 'Cliente atualizado com sucesso!', 'data': getByCode(data['CODCLI'])}, 200
        except Exception as e:
            return {'message': 'Erro na tentativa de atualização', 'error': str(e)}, 500
        
        