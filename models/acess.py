from sql_alchemy import database
import datetime

from models.user import UserModel

class AcessModel(database.Model):
    __tablename__ = 'acess'
    
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    date = database.Column(database.DateTime, default=datetime.datetime.now())
    user_id = database.Column(database.String, database.ForeignKey('users.id'))
    nome_vend = database.Column(database.String, nullable=False)
    table_changed = database.Column(database.String)
    type_of_change = database.Column(database.String)
    response_time = database.Column(database.Integer)
    
    def __init__(self, user_id, table_changed, type_of_change, response_time):
        user = UserModel.findUser(user_id)
        if user:
            self.user_id = user.user_id
            self.nome_vend = user.nome_vend
        else:
            self.user_id = user_id
            self.nomeVend = ''
            
        self.table_changed = table_changed
        self.type_of_change = type_of_change
        self.response_time = response_time
        
        self.date = datetime.datetime.now()
        
        
    def saveAcess(self):
        database.session.add(self)
        database.session.commit()
        