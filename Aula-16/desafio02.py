# Desafio-2
# Crie um dicionário que represente o estoque de uma loja, com produtos como chaves e quantidades em estoque como valores.
# Permita que o usuário insira um produto e verifique se ele está em estoque.
# Se estiver, informe a quantidade em estoque; caso contrário, informe que o produto não está disponível.
estoque_loja = {
    "maçã": 50,
    "banana": 30,
    "laranja": 20,
    "uva": 15
}

produto = input("Digite o nome do produto: ")

if produto in estoque_loja:
    print("Quantidade em estoque:", estoque_loja[produto])
else:
    print("Produto não disponível.")
