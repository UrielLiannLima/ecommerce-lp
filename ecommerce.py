from enum import Enum

#Enumeração de MarcaProduto
class MarcaProduto(Enum):
    Intriseca = 1
    SONY = 2
    Tarkett = 3

#Classe base Produto com o método construtor
class Produto:
    def __init__(self, codigoBarras, nome, preco, marca):
        self.codigoBarras = codigoBarras
        self.nome = nome
        self.preco = preco
        self.marca = marca