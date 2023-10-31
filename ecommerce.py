from enum import Enum

#Enumeração de MarcaProduto
class MarcaProduto(Enum):
    Intriseca = 1
    SONY = 2
    Tarkett = 3

#Classe base Produto com o método construtor, com os métodos getter e setter para cada atributo
class Produto:
    def __init__(self, codigoBarras, nome, preco, marca):
        self.codigoBarras = codigoBarras
        self.nome = nome
        self.preco = preco
        self.marca = marca
    
    def getCodigoBarras(self):
        return self.codigoBarras

    def setCodigoBarras(self, codigoBarras):
        self.codigoBarras = codigoBarras

    def getNome(self):
        return self.nome

    def setNome(self, nome):
        self.nome = nome

    def getPreco(self):
        return self.preco

    def setPreco(self, preco):
        self.preco = preco

    def getMarca(self):
        return self.marca

    def setMarca(self, marca):
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

#Classe Estoque que gerencia o estoque de produtos
class Estoque:
    def __init__(self):
        self.produtos = {}  #Dicionário para manter o estoque

    def adicionarProduto(self, produto, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        if produto.getCodigoBarras() in self.produtos:
            self.produtos[produto.getCodigoBarras()] += quantidade
        else:
            self.produtos[produto.getCodigoBarras()] = quantidade

    def venderProduto(self, codigoBarras, quantidade):
        if codigoBarras not in self.produtos:
            raise Exception("Produto não está no estoque.")
        
        if self.produtos[codigoBarras] < quantidade:
            raise Exception("Quantidade insuficiente para venda.")
        
        self.produtos[codigoBarras] -= quantidade

    def devolverProduto(self, codigoBarras, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        if codigoBarras not in self.produtos:
            raise Exception("Produto não está no estoque.")
        
        self.produtos[codigoBarras] += quantidade

    def reabastecerProduto(self, codigoBarras, quantidade):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")
        
        if codigoBarras in self.produtos:
            self.produtos[codigoBarras] += quantidade
        else:
            raise Exception("Produto não encontrado para reabastecimento.")

    def mostrarEstoque(self):
        print("\nEstado atual do estoque:")
        for codigoBarras, quantidade in self.produtos.items():
            print(f"Código de Barras: {codigoBarras}, Quantidade: {quantidade}")
            
#Exemplo de uso:
estoque = Estoque()

# Adicionar produtos ao estoque
produto1 = Livros(1, "Uma Questão de Química", 31, MarcaProduto.Intriseca, "Isabelli Cristhini")
produto2 = DVD(2, "A Era do Gelo", 10, MarcaProduto.SONY, "João Otávio")
produto3 = Vinil(3, "Tequila", 69, MarcaProduto.Tarkett, "Uriel L.")

estoque.adicionarProduto(produto1, 13)
estoque.adicionarProduto(produto2, 22)
estoque.adicionarProduto(produto3, 420)