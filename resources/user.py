from flask_restful import Resource, reqparse
from flask import request
from datetime import date
from flask_jwt_extended import create_access_token, jwt_required
import datetime

from models.user import UserModel
from models.acess import AcessModel
from models.userInfo2 import UserInfo as ui

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

        acessToken = None
        if user.flag_have_acess:
            
            acessToken = create_access_token(identity={
                                            'user': user.id}, expires_delta=datetime.timedelta(hours=9))
        
        return {"flag_have_acess": user.flag_have_acess, "acessToken": acessToken, "user": user.to_json()}, 200

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
    # @jwt_required()
    def get(self):
        # userId = get_jwt()['identity']['userId']

        # user = UserModel.findUser('userId')
        user = UserModel.find_user('914e9e5377230fb7')
        
        user_info = ui(user)
        # start_date, end_date = date(2021, 1, 1), date(2021, 1, 31)
        
        print(user_info.as_json())
        
        
        # print(user_info.sales_count(start_date, end_date))
        # print(user_info.devolution_count(start_date, end_date))
        
        # print(user_info.sales_comission(start_date, end_date))
        # print(user_info.devolution_comission(start_date, end_date))

        # try:
        #     data = getUserInfo(user)
        # except Exception as e:
        #     return {'message': 'Erro ao carregar informações', 'error': str(e)}, 500

        # return data, 200
