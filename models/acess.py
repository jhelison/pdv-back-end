from sql_alchemy import database
import datetime

class AcessModel(database.Model):
    __tablename__ = 'acess'
    
    acess_id = database.Column(database.Integer, primary_key=True, autoincrement=True)
    date = database.Column(database.DateTime, default=datetime.datetime.now())
    userId = database.Column(database.String, database.ForeignKey('users.userId'))
    nomeVend = database.Column(database.String, nullable=False)
    
    def __init__(self, userId, nomeVend, date):
        self.userId = userId
        self.nomeVend = nomeVend
        self.date = date
        
    def saveAcess(self):
        database.session.add(self)
        database.session.commit()
        