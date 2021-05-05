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
    comission_multiplier = database.Column(
        database.Float(precision=1), default=1.0)
    max_discount = database.Column(database.Float(precision=2))
    flag_see_all_budgets = database.Column(database.Boolean, default=False)
    flag_have_acess = database.Column(database.Boolean, default=False)
    insert_date = database.Column(database.DateTime)
    admissional_date = database.Column(database.Date)
    last_update = database.Column(database.DateTime)

    def __init__(self, id, profile_name, platform, phone_model, cod_vend, nome_vend):
        self.id = id
        self.profile_name = profile_name
        self.platform = platform
        self.phone_model = phone_model
        self.cod_vend = cod_vend
        self.nome_vend = nome_vend

        self.insert_date = datetime.datetime.now()
        self.last_update = datetime.datetime.now()

    @classmethod
    def find_user(cls, id):
        user = cls.query.filter_by(id=id).first()
        if user:
            return user
        return None

    @classmethod
    def count_users(cls):
        return cls.query.count()

    def save_user(self):
        database.session.add(self)
        database.session.commit()

    def delete_user(self):
        database.session.delete(self)
        database.session.commit()

    def update_user(self, data):
        for key in data.keys():
            if key == "insert_date":
                self.insert_date = datetime.datetime.strptime(data[key], "%Y-%m-%d %H:%M:%S.%f")
                continue
            if key == "admissional_date":
                self.admissional_date = datetime.datetime.strptime(data[key].split("T")[0], "%Y-%m-%d")
                continue
            if key == "last_update":
                self.last_update = datetime.datetime.now()
                continue

            setattr(self, key, data[key])
        database.session.commit()

    def to_json(self):
        return {
            "id": self.id,
            "profile_name": self.profile_name,
            "platform": self.platform,
            "phone_model": self.phone_model,
            "cod_vend": self.cod_vend,
            "nome_vend": self.nome_vend,
            "salary": self.salary,
            "comission_objective": self.comission_objective,
            "comission_multiplier": self.comission_multiplier,
            "max_discount": self.max_discount,
            "flag_see_all_budgets": self.flag_see_all_budgets,
            "flag_have_acess": self.flag_have_acess,
            "insert_date": str(self.insert_date) if self.insert_date else "",
            "admissional_date": str(self.admissional_date) if self.admissional_date else "",
            "last_update": str(self.last_update) if self.last_update else ""
        }
