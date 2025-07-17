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
def menu():
    while True:
        menu = input(f'''
                        1 - ver estoque
                        2 - adicionar ao estoque
                        3 - remover do estoque
                        4 - subtrair do estoque
                        5 - sair  
                        Digite a entrada:''')
        if menu == '1':
            verEstoque()
        elif menu == '2':
            adcEstoque()
        elif menu == '3':
            rmvEstoque()
        elif menu == '4':
            dimEstoque()
        elif menu == '5':
            return

def verEstoque():
    print(estoque_loja)

def adcEstoque():
    adcProduto = input("Escreva o produto que deseja adicionar:")
    qtdProduto = int(input("Digite a quantidade a ser adicionada ao estoque:"))    
    estoque_loja[adcProduto] = qtdProduto
    if adcProduto in estoque_loja:
        qtdProduto += qtdProduto
    
    print(estoque_loja)    

def rmvEstoque():   
    remover = input("Digite o item a ser removido:") 
    del estoque_loja[remover]
    
def dimEstoque():
    ant = 2
    print(ant)



# produto = input("Digite o nome do produto: ")

# if produto in estoque_loja:
#     print("Quantidade em estoque:", estoque_loja[produto])
# else:
#     print("Produto não disponível.")
menu()