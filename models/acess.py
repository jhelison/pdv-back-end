from sql_alchemy import database
import datetime

from models.user import UserModel

class AcessModel(database.Model):
    __tablename__ = 'acess'
    
    id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    date = database.Column(database.DateTime, default=datetime.datetime.now())
    user_id = database.Column(database.String, database.ForeignKey('users.userId'))
    nome_vend = database.Column(database.String, nullable=False)
    table_changed = database.Column(database.String)
    type_of_change = database.Column(database.String)
    
    def __init__(self, userId, acessMethod):
        user = UserModel.findUser(userId)
        if user:
            self.userId = user.userId
            self.nomeVend = user.nomeVend
        else:
            self.userId = userId
            self.nomeVend = ''
            
        self.date = datetime.datetime.now()
        self.acessMethod = acessMethod
        
    def saveAcess(self):
        database.session.add(self)
        database.session.commit()
        