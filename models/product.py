from __future__ import annotations
import sys
from typing import Union
sys.path.insert(0, './')
from utility.FDB_handler import FDBModel, Column

# QUERY = """
#         SELECT 
#             PRODUTO.CODPROD, 
#             PRODUTO.CODIGO, 
#             PRODUTO.NOMEPROD, 
#             PRODUTO.UNIDADE, 
#             PRODUTO.DESCMAXIMO, 
#             PRODUTOESTOQUE.ESTATU, 
#             PRODUTOPRECO.PRECO,
#             PRODUTO.FLAGINATIVO
#         FROM 
#             PRODUTO
#         LEFT JOIN 
#             PRODUTOESTOQUE ON 
#                 PRODUTO.CODPROD = PRODUTOESTOQUE.CODPROD
#         LEFT JOIN 
#             PRODUTOPRECO ON 
#                 PRODUTO.CODPROD = PRODUTOPRECO.CODPROD
#         WHERE PRODUTOESTOQUE.CODEMPRESA = 1
#         AND PRODUTOPRECO.CODPRECO = '000000001'"""

class Product(FDBModel):
    __tablename__ = "PRODUTO"
    
    CODPROD = Column(is_primary_key=True)
    CODIGO = Column()
    NOMEPROD = Column()
    UNIDADE = Column()
    DESCMAXIMO = Column()
    FLAGINATIVO = Column()

    def __init__(self,
                 CODPROD: str,
                 CODIGO: str,
                 NOMEPROD: str,
                 UNIDADE: str,
                 DESCMAXIMO: int,
                 FLAGINATIVO: Union[str, bool]
                 ):
        self.CODPROD = CODPROD
        self.CODIGO = CODIGO
        self.NOMEPROD = NOMEPROD
        self.UNIDADE = UNIDADE
        self.DESCMAXIMO = DESCMAXIMO
        self.FLAGINATIVO = FLAGINATIVO

        if isinstance(FLAGINATIVO, str):
            self.FLAGINATIVO = FLAGINATIVO == "Y"
        else:
            self.FLAGINATIVO = FLAGINATIVO
            
    def json(self):
        stock = self.get_stock()
        price = self.get_price()
        
        return self.convert_to_JSON({
            'CODPROD': self.CODPROD,
            'CODIGO': self.CODIGO,
            'NOMEPROD': self.NOMEPROD,
            'UNIDADE': self.UNIDADE,
            'DESCMAXIMO': self.DESCMAXIMO,
            'FLAGINATIVO': self.FLAGINATIVO,
            'ESTOQUE': stock.ESTATU if stock else None,
            'PRECO': price.PRECO if price else None
        })
        
    def get_stock(self) -> ProductStock:
        product_stock = ProductStock.find_by_columns(CODPROD = self.CODPROD, CODEMPRESA = 1)
        if product_stock:
            return product_stock[0]
        return None
    
    def get_price(self) -> ProductPrice:
        product_price = ProductPrice.find_by_columns(CODPROD = self.CODPROD, CODPRECO = "000000001")
        if product_price:
            return product_price[0]
        return None
        
class ProductStock(FDBModel):
    __tablename__ = "PRODUTOESTOQUE"
    
    CODPROD = Column(is_primary_key=True)
    CODEMPRESA = Column()
    CODSETORESTOQUE = Column()
    ESTATU = Column()
    
    def __init__(self, CODPROD, CODEMPRESA, CODSETORESTOQUE, ESTATU) -> None:
        self.CODEMPRESA = CODEMPRESA
        self.CODPROD = CODPROD 
        self.CODSETORESTOQUE = CODSETORESTOQUE
        self.ESTATU = ESTATU
    
class ProductPrice(FDBModel):
    __tablename__ = "PRODUTOPRECO"
    
    CODPRODUTOPRECO = Column(is_primary_key=True)
    CODPROD = Column()
    CODPRECO = Column()
    PRECO = Column()
    
    def __init__(self, CODPRODUTOPRECO, CODPROD, CODPRECO, PRECO):
        self.CODPRODUTOPRECO = CODPRODUTOPRECO
        self.CODPROD = CODPROD
        self.CODPRECO = CODPRECO
        self.PRECO = PRECO