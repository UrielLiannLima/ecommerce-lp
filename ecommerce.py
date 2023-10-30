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
        
#Classes especializadas herdando de Produto, cada uma com um atributo único para si
class Livros(Produto):
    def __init__(self, codigoBarras, nome, preco, marca, autor):
        super().__init__(codigoBarras, nome, preco, marca)
        self.autor = autor

class DVD(Produto):
    def __init__(self, codigoBarras, nome, preco, marca, diretor):
        super().__init__(codigoBarras, nome, preco, marca)
        self.diretor = diretor

class Vinil(Produto):
    def __init__(self, codigoBarras, nome, preco, marca, musica):
        super().__init__(codigoBarras, nome, preco, marca)
        self.musica = musica
