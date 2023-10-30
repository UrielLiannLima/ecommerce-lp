import ecommerce

estoque = Estoque()

# Adicionar produtos ao estoque
produto1 = Eletronicos(1, "Laptop", 1000, MarcaProduto.MARCA_A, "Bateria")
produto2 = Vestuario(2, "Camiseta", 20, MarcaProduto.MARCA_B, "M")
produto3 = Livros(3, "Python para Iniciantes", 30, MarcaProduto.MARCA_C, "João Silva")

estoque.adicionar_produto(produto1, 10)
estoque.adicionar_produto(produto2, 50)
estoque.adicionar_produto(produto3, 100)

# Vender um produto
try:
    estoque.vender_produto(2, 3)
    print("Venda realizada com sucesso.")
except Exception as e:
    print(f"Erro ao vender: {e}")

# Devolver um produto
try:
    estoque.devolver_produto(2, 2)
    print("Produto devolvido com sucesso.")
except Exception as e:
    print(f"Erro ao devolver: {e}")

# Reabastecer um produto
try:
    estoque.reabastecer_produto(1, 5)
    print("Reabastecimento realizado com sucesso.")
except Exception as e:
    print(f"Erro ao reabastecer: {e}")

# Exibir o estado atual do estoque
print("\nEstado atual do estoque:")
for codigo_de_barras, quantidade in estoque.produtos.items():
    print(f"Código de Barras: {codigo_de_barras}, Quantidade: {quantidade}")