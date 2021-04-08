from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt

from models.topItems import getTopItems

class TopItems(Resource):
    
    @jwt_required
    def get(self):
        codvend = get_jwt()['identity']['codvend']
                
        try:
            data = getTopItems(codvend)
        except Exception as e:
            return {'message': 'Erro ao carregar informações', 'error': str(e)}, 500
        
        
        return data, 200