
from datetime import datetime
import sys

sys.path.insert(0, './')

from utility.FDB_handler import Column, FDBModel

class Customer(FDBModel):
    __tablename__ = "CLIENTE"
    
    CODCLI = Column(is_primary_key=True, use_table_codigo=8)
    CODIGO = Column(is_primary_key=True, use_table_codigo=6)
    NOMECLI = Column()
    ENDERECO = Column()
    BAIRRO = Column()
    CIDADE = Column()
    ESTADO = Column()
    CEP = Column()
    TELEFONE = Column()
    CNPJ = Column()
    CPF = Column()
    INSCR = Column()
    FLAGFISICA = Column()
    DATCAD = Column()
    LAST_CHANGE = Column()
    EMAIL = Column()
    CONJFANTASIA = Column()
    NUMEROLOGRADOURO = Column()
    COMPLEMENTOLOGRADOURO = Column()
    
    def __init__(self,
                CODCLI,
                CODIGO,
                NOMECLI,
                ENDERECO = None,
                BAIRRO = None,
                CIDADE = None,
                ESTADO = None,
                CEP = None,
                TELEFONE = None,
                CNPJ = None,
                CPF = None,
                INSCR = None,
                FLAGFISICA = None,
                DATCAD = None,
                LAST_CHANGE = None,
                EMAIL = None,
                CONJFANTASIA = None,
                NUMEROLOGRADOURO = None,
                COMPLEMENTOLOGRADOURO = None) -> None:
        
        self.CODCLI = CODCLI
        self.CODIGO = CODIGO
        self.NOMECLI = NOMECLI
        self.ENDERECO = ENDERECO
        self.BAIRRO = BAIRRO
        self.CIDADE = CIDADE
        self.ESTADO = ESTADO
        self.CEP = CEP
        self.TELEFONE = TELEFONE
        self.CNPJ = CNPJ
        self.CPF = CPF
        self.INSCR = INSCR
        self.FLAGFISICA = FLAGFISICA
        self.DATCAD = DATCAD
        self.LAST_CHANGE = LAST_CHANGE
        self.EMAIL = EMAIL
        self.CONJFANTASIA = CONJFANTASIA
        self.NUMEROLOGRADOURO = NUMEROLOGRADOURO
        self.COMPLEMENTOLOGRADOURO = COMPLEMENTOLOGRADOURO
        
    def json(self) -> str:
        return self.convert_to_JSON({
            'CODCLI': self.CODCLI,
            'CODIGO': self.CODIGO,
            'NOMECLI': self.NOMECLI,
            'ENDERECO': self.ENDERECO,
            'BAIRRO': self.BAIRRO,
            'CIDADE': self.CIDADE,
            'ESTADO': self.ESTADO,
            'CEP': self.CEP,
            'TELEFONE': self.TELEFONE,
            'CNPJ': self.CNPJ,
            'CPF': self.CPF,
            'INSCR': self.INSCR,
            'FLAGFISICA': self.FLAGFISICA,
            'DATCAD': self.DATCAD,
            'LAST_CHANGE': self.LAST_CHANGE,
            'EMAIL': self.EMAIL,
            'CONJFANTASIA': self.CONJFANTASIA,
            'NUMEROLOGRADOURO': self.NUMEROLOGRADOURO,
            'COMPLEMENTOLOGRADOURO': self.COMPLEMENTOLOGRADOURO
        })
    
    def _on_update(self) -> None:
        self.LAST_CHANGE = datetime.now()