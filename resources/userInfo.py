from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_raw_jwt

from models.user import UserModel
from models.userInfo import getUserInfo

class UserInfo(Resource):
    
    @jwt_required
    def get(self):
        userId = get_raw_jwt()['identity']['userId']
        
        user = UserModel.findUser(userId)
        
        try:
            data = getUserInfo(user)
        except Exception as e:
            return {'message': 'Erro ao carregar informações', 'error': str(e)}, 500
        
        
        return data, 200