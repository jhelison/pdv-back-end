from flask_restful import Resource, reqparse
from flask import request
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
            users = UserModel.query.order_by(UserModel.insert_date.desc()).all()
        except Exception as e:
            return {'message': 'Erro ao obter todos os usuarios', 'error': str(e)}, 500

        return [user.to_json() for user in users]


class User(Resource):
    args = reqparse.RequestParser()
    args.add_argument('id')

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
                                         'user': user.to_json()}, expires_delta=datetime.timedelta(hours=9))
        
        return acessToken, 200

    def post(self):
        """
        Recieve as
	    "content": {
            "id": ,
            "profile_name": ,
            "platform": ,
            "phone_model": ,
            "cod_vend": ,
            "nome_vend": 
	    }
        """
        content = request.get_json()["content"]

        try:
            if(not UserModel.find_user(content['id'])):
                newUser = UserModel(**content)
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
        id = request.get_json()["id"]

        try:
            user = UserModel.find_user(id)
            if user:
                user.delete_user()
            else:
                return {'message': 'Usuario não encontrado'}, 404
        except Exception as e:
            return {'message': 'Erro ao pesquisar o usuario', 'error': str(e)}, 500

        return user.to_json(), 200

    def put(self):
        """
        Recieves
        "id": ...,
        "content": {}
        """
        id = request.get_json()["id"]
        content = request.get_json()["content"]

        print(id)
        print(content)

        try:
            user = UserModel.find_user(id)
            if user:
                user.update_user(content)
            else:
                return {'message': 'Usuario não encontrado'}, 404
        except Exception as e:
            print(e)
            return {'message': 'Erro ao pesquisar o cliente', 'error': str(e)}, 500
        
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
