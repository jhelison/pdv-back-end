from __future__ import annotations
import sys

sys.path.insert(0, './')
from utility.FDB_handler import FDBHandler


class FDBModel:
    __tablename__ = None
    
    @classmethod
    def find_exact(cls, *args, **kwargs):
        print(cls, [type(value) for value in cls.__dict__.values()])
        return cls.__tablename__

class Column:
    def __init__(self, name, age):
      self.name = name
      self.age = age

class Seller(FDBModel):
    __tablename__ = "VENDEDOR"
    
    CODVENDED = None
    NOMEVENDED = None
    INATIVO = None
    
    def __init__(self, CODVENDED: str, NOMEVENDED: str, INATIVO: str):
        self.CODVENDED = CODVENDED
        self.NOMEVENDED = NOMEVENDED
        self.INATIVO = INATIVO
        
    def json(self):
        return FDBHandler.convert_to_JSON({
            'CODVENDED': self.CODVENDED,
            'NOMEVENDED': self.NOMEVENDED,
            'INATIVO': self.INATIVO 
        })

    @classmethod
    def teste(cls):
        return cls.show_table_name()

    @classmethod
    def all(cls):
        query = """
        SELECT 
            CODVENDED, NOMEVENDED, INATIVO
        FROM
            VENDEDOR
        """
        
        res = FDBHandler().fetchall_as_dict(query)
        
        return [Seller(**row) for row in res]
        
    @classmethod
    def find(cls, CODVENDED: str):
        query = """
        SELECT 
            CODVENDED, NOMEVENDED, INATIVO
        FROM 
            VENDEDOR
        WHERE 
            CODVENDED = ?
        """
        
        params = [CODVENDED]
        
        res = FDBHandler().fetchone_as_dict(query, params)
        
        return Seller(**res)
    
print(Seller.teste())