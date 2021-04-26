from flask_restful import Resource, reqparse
import json
from flask_jwt_extended import create_access_token, jwt_required
import datetime

from models.user import UserModel
from models.acess import AcessModel
from models.userInfo import getUserInfo

class Users(Resource):
    def get(self):
        """
        Returns [{
            "id": id,
            "profile_name": profile_name,
            "platform": platform,
            "phone_model": phone_model,
            "cod_vend": cod_vend,
            "nome_vend": nome_vend,
            "salary": salary,
            "comission_objective": comission_objective,
            "comission_multiplier": comission_multiplier,
            "max_discount": max_discount,
            "flag_see_all_budgets": flag_see_all_budgets,
            "flag_have_acess": flag_have_acess,
            "insert_date": insert_date,
            "admissional_date": admissional_date,
            "last_update": last_update
        }, ...]
        """
        try:
            users = UserModel.query.all()
        except Exception as e:
            return {'message': 'Erro ao obter todos os usuarios', 'error': str(e)}, 500

        return [user.to_json() for user in users]


class User(Resource):
    args = reqparse.RequestParser()
    args.add_argument('id', type=str, required=False,
                      help="The field data cant be empty")
    args.add_argument('data', type=str, required=False,
                      help="The field data cant be empty")

    def get(self):
        id = User.args.parse_args()['id']

        try:
            user = UserModel.find_user(id)
        except Exception as e:
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500

        if(not user):
            return {'message': 'Usuario não encontrado'}, 404

        if(not user.flag_have_acess):
            return {'message': 'Acesso não autorizado'}, 401

        acessToken = create_access_token(identity={
                                         'id': user.id, 'codvend': user.codvend, 'flagAdmin': user.flagAdmin}, expires_delta=datetime.timedelta(hours=9))
        
        return acessToken, 200

    def put(self):
        """
        Recieve as
	    "data": {
            "id": ,
            "profile_name": ,
            "platform": ,
            "phone_model": ,
            "cod_vend": ,
            "nome_vend": 
	    }
        """
        data = json.loads(User.args.parse_args().data)

        try:
            if(not UserModel.find_user(data['id'])):
                newUser = UserModel(**data)
                newUser.save_user()
            else:
                return {'message': 'Usuario já existe'}, 400

        except Exception as e:
            return {'message': 'Erro ao pesquisar o usuario', 'error': str(e)}, 500

        return newUser.to_json(), 201
    
    def delete(self):
        """
        Recieves
        "id": ...
        """
        id = User.args.parse_args()['id']

        try:
            user = UserModel.find_user(id)
            if user:
                user.delete_user()
            else:
                return {'message': 'Usuario não encontrado'}, 404
        except Exception as e:
            return {'message': 'Erro ao pesquisar o usuario', 'error': str(e)}, 500

        return user.to_json(), 200




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
