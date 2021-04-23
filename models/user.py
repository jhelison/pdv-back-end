from sql_alchemy import database
import datetime


class UserModel(database.Model):
    __tablename__ = 'users'

    id = database.Column(database.String, primary_key=True)
    profileName = database.Column(database.String(80), nullable=False)
    platform = database.Column(database.String, nullable=False)
    phoneModel = database.Column(database.String, nullable=False)
    codVend = database.Column(database.String, nullable=False)
    nomeVend = database.Column(database.String, nullable=False)
    salary = database.Column(database.Float(precision=2))
    comissionObjective = database.Column(database.Float(precision=2))
    comissionMult = database.Column(database.Float(precision=1), default=1.0)
    maxDiscount = database.Column(database.Float(precision=2))
    flagSeeAllBudgets = database.Column(database.Boolean, default=False)
    flagHaveAcess = database.Column(database.Boolean, default=False)
    insertDate = database.Column(
        database.DateTime, default=datetime.datetime.now())
    admissionalDate = database.Column(database.Date)

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
