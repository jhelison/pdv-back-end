from __future__ import annotations
from collections import defaultdict
import json
from typing import List, Tuple, Union, Type, TypeVar
import fdb
from decimal import Decimal
import datetime

PATH = r'C:\Users\jheli\Documents\programming-projects\PDV\temp\CPLUS.FDB'

con = None

T = TypeVar('T', bound='TrivialClass')

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

    def fetchall_as_dict(self, query: str, params: list = [], one_key: bool = False) -> dict:
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

    def fetchone_as_dict(self, query: str, params: list = []) -> dict:
        """
        Accepts query and params and fetch one row returning a dict with the data.
        """
        cur = self.con.cursor()
        cur.execute(query, params)
        coumns_names = [row[0] for row in cur.description]

        data = cur.fetchone()
        cur.close()

        return {coumns_names[idx]: data[idx] for idx in range(len(data))}


class FDBModel:
    __tablename__ = None

    @classmethod
    def all(cls: Type[T]) -> List[T]:
        query = cls._basic_query()

        res = FDBHandler().fetchall_as_dict(query)

        return [cls(**row) for row in res]

    @classmethod
    def find_by_key(cls: Type[T], key_value: Union[str, int]) -> T:
        primary_key = cls._get_primary_key()

        if not primary_key:
            error = f"Primary key is missing for the class {cls.__class__.__name__}"
            raise TypeError(error)

        query = cls._basic_query()
        query += f" WHERE {primary_key[0]} = ?"

        res = FDBHandler().fetchone_as_dict(query, [key_value])

        return cls(**res)

    @classmethod
    def find_by_columns(cls: Type[T], exact: bool = True, **kwargs) -> List[T]:
        if kwargs:
            columns = cls._get_columns()

            wheres = []
            params = []

            for key in kwargs:
                if key in columns:
                    q, p = cls._build_where(kwargs[key], key, exact)
                    wheres.append(q)
                    params += p

            query = cls._basic_query()
            query += "WHERE " + " AND ".join(wheres)
            
            res = FDBHandler().fetchall_as_dict(query, params)
            return [cls(**row) for row in res]
        else:
            return None

    @classmethod
    def _basic_query(cls) -> str:
        return """
        SELECT
            {}
        FROM
            {}
        """.format(", ".join([column for column in cls._get_columns()]), cls.__tablename__)

    @classmethod
    def _get_primary_key(cls) -> str:
        return [key for key, value in cls.__dict__.items() if isinstance(value, Column) and value.is_primary_key]

    @classmethod
    def _get_columns(cls) -> list:
        return [key for key, value in cls.__dict__.items() if isinstance(value, Column)]

    @staticmethod
    def convert_to_JSON(data: dict) -> str:
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

    @staticmethod
    def _build_where(value: Union[str, int, float], column: str, exact: bool = True) -> Tuple[str, Tuple[str]]:
        query = []
        params = []

        if exact:
            return f"{column} = ?", [value]
        else:
            splited = value.split(' ')
            for word in splited:
                query.append(f"{column} SIMILAR TO '%{word}%'")

            return " AND ".join(query), params


class Column:
    def __init__(self, is_primary_key: bool = False) -> None:
        self.is_primary_key = is_primary_key
