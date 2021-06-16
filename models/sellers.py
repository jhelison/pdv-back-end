from __future__ import annotations
from typing import Union
import sys

sys.path.insert(0, './')

from utility.FDB_handler import Column, FDBModel

class Seller(FDBModel):
    __tablename__ = "VENDEDOR"
    
    CODVENDED = Column(is_primary_key=True)
    NOMEVENDED = Column()
    INATIVO = Column()
    
    def __init__(self, CODVENDED: str, NOMEVENDED: str, INATIVO: Union[str, bool]):
        self.CODVENDED = CODVENDED
        self.NOMEVENDED = NOMEVENDED
        self.INATIVO = INATIVO
        
    def json(self):
        return self.convert_to_JSON({
            'CODVENDED': self.CODVENDED,
            'NOMEVENDED': self.NOMEVENDED,
            'INATIVO': self.INATIVO 
        })