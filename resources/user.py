from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import create_access_token, jwt_required
import datetime

from models.user import UserModel
from models.acess import AcessModel
from models.userInfo import getUserInfo


class User(Resource):
    args = reqparse.RequestParser()
    args.add_argument('userId', type=str, required=False,
                      help="The field data cant be empty")
    args.add_argument('data', type=str, required=False,
                      help="The field data cant be empty")

    def get(self):
        userId = User.args.parse_args()['userId']

        try:
            user = UserModel.findUser(userId)
            if(user and user.flagHaveAcess):
                acess = AcessModel(user.userId, 'userGET')
                acess.saveAcess()
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500

        if(not user):
            return {'message': 'Usuario não encontrado'}, 404

        if(not user.flagHaveAcess):
            return {'message': 'Acesso não autorizado'}, 401

        acessToken = create_access_token(identity={
                                         'userId': user.userId, 'codvend': user.codvend, 'flagAdmin': user.flagAdmin}, expires_delta=datetime.timedelta(hours=9))
        return acessToken, 200

    def put(self):
        data = json.loads(User.args.parse_args().data)

        try:
            if(not UserModel.findUser(data['userId'])):
                newUser = UserModel(**data)
                newUser.saveUser()

        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500


class UserInfo(Resource):

    @jwt_required()
    def get(self):
        userId = get_jwt()['identity']['userId']

        user = UserModel.findUser(userId)

        try:
            data = getUserInfo(user)
        except Exception as e:
            return {'message': 'Erro ao carregar informações', 'error': str(e)}, 500

        return data, 200
