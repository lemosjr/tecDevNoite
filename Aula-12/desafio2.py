# O Sr. Manoel Joaquim acaba de adquirir uma panificadora
# e pretende implantar a metodologia da tabelinha, que já é um sucesso na sua loja de 1,99.
# Você foi contratado para desenvolver o programa que monta a tabela de preços de
# pães, de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo abaixo:
# Preço do pão: R$ 0.18
# Panificadora Pão de Ontem - Tabela de preços
# 1 - R$ 0.18
# 2 - R$ 0.36
# ...

# 50 - R$ 9.00
menu = int(input("Digite 1 para gerar a tabela de preços ou 2 para sair: "))
while True:
    if menu == 1:
        print("Lojas Quase Dois - Tabela de preços")
        for i in range(1, 51):
            preco = i * 0.18
            print(f"{i} - R$ {preco:.2f}")
        break
    elif menu == 2:
        print("Saindo do programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
        menu = int(input("Digite 1 para gerar a tabela de preços ou 2 para sair: "))