from array import array
from collections import defaultdict
import json
import fdb
from decimal import Decimal
import datetime

path = r'C:\Users\jheli\Documents\programming-projects\PDV\temp\CPLUS.FDB'
con = fdb.connect(path, 'SYSDBA', 'masterkey')

def fetchall_as_dict(query: str, params: array = [], one_key: bool = False) -> dict:
    """
    Accepts query and params and fetch all the rows returning a dict with the data.
    one_key groups all the keys into arrays.
    """

    cur = con.cursor().execute(query, params)
    coumns_names = [row[0] for row in cur.description]

    data = cur.fetchall()

    if one_key:
        data_dict = defaultdict(list)
        for row in data:
            for idx in range(len(row)):
                data_dict[coumns_names[idx]].append(row[idx])
        return dict(data_dict)
    return [{coumns_names[idx]:row[idx] for idx in range(len(row))} for row in data]

def fetchone_as_dict(query: str, params: array = []) -> dict:
    """
    Accepts query and params and fetch one row returning a dict with the data.
    """
    cur = con.cursor().execute(query, params)
    coumns_names = [row[0] for row in cur.description]

    data = cur.fetchone()

    return {coumns_names[idx]:data[idx] for idx in range(len(data))}

def convert_to_JSON(data: dict) -> dict:
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