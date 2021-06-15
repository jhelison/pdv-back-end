from array import array
from collections import defaultdict
import json
import fdb
from decimal import Decimal
import datetime

from sqlalchemy.orm import query

PATH = r'C:\Users\jheli\Documents\programming-projects\PDV\temp\CPLUS.FDB'

con = None

class Singleton(type):
    _instances: dict = {}

    def __call__(cls, *args, **kwds) -> None:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwds)
        return cls._instances[cls]

class FDBHandler(metaclass=Singleton):
    """
    Build a new connection to the database
    """
    def __init__(self) -> None:
        self.con = fdb.connect(PATH, 'SYSDBA', 'masterkey')

    def fetchall_as_dict(self, query: str, params: array = [], one_key: bool = False) -> dict:
        """
        Accepts query and params and fetch all the rows returning a dict with the data.
        one_key groups all the keys into arrays.
        """
        cur = self.con.cursor()
        cur.execute(query, params)
        coumns_names = [row[0] for row in cur.description]

        data = cur.fetchall()
        cur.close()

        if one_key:
            data_dict = defaultdict(list)
            for row in data:
                for idx in range(len(row)):
                    data_dict[coumns_names[idx]].append(row[idx])
            return dict(data_dict)
        return [{coumns_names[idx]:row[idx] for idx in range(len(row))} for row in data]

    def fetchone_as_dict(self, query: str, params: array = []) -> dict:
        """
        Accepts query and params and fetch one row returning a dict with the data.
        """
        cur = self.con.cursor()
        cur.execute(query, params)
        coumns_names = [row[0] for row in cur.description]

        data = cur.fetchone()
        cur.close()

        return {coumns_names[idx]:data[idx] for idx in range(len(data))}

    @classmethod
    def convert_to_JSON(cls, data: dict) -> dict:
        """
        Convert dict to a array parsing the data.
        Accepts arrays of dicts or dict as input.
        """
        def data_type_handler(x):
            if isinstance(x, Decimal):
                return float(x)
            elif isinstance(x, datetime.datetime):
                return x.strftime("%Y-%m-%d %H:%M:%S")
            elif isinstance(x, datetime.date):
                return x.strftime("%Y-%m-%d")
            elif isinstance(x, datetime.time):
                return x.strftime("%H:%M:%S")   

        return json.dumps(data, default=data_type_handler)