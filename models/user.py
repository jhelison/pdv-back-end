from sql_alchemy import database
import datetime


class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.String, primary_key=True)
    profile_name = database.Column(database.String(80), nullable=False)
    platform = database.Column(database.String, nullable=False)
    phone_model = database.Column(database.String, nullable=False)
    cod_vend = database.Column(database.String, nullable=False)
    nome_vend = database.Column(database.String, nullable=False)
    salary = database.Column(database.Float(precision=2))
    comission_objective = database.Column(database.Float(precision=2))
    comission_multiplier = database.Column(database.Float(precision=1), default=1.0)
    max_discount = database.Column(database.Float(precision=2))
    flag_see_all_budgets = database.Column(database.Boolean, default=False)
    flag_have_acess = database.Column(database.Boolean, default=False)
    insert_date = database.Column(
        database.DateTime, default=datetime.datetime.now())
    admissional_date = database.Column(database.Date)
    last_update = database.Column(database.Date)

    def __init__(self, userId, profileName, platform, phoneModel, codvend, nomeVend):
        self.userId = userId
        self.profileName = profileName
        self.platform = platform
        self.phoneModel = phoneModel
        self.codvend = codvend
        self.nomeVend = nomeVend

    @classmethod
    def findUser(cls, userId):
        user = cls.query.filter_by(userId=userId).first()
        if user:
            return user
        return None

    def saveUser(self):
        database.session.add(self)
        database.session.commit()
