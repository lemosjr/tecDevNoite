# 2. Crie um programa em Python que simule um sistema de chamada de senhas em um laboratório.
# O programa deve apresentar um menu com três opções: criar nova senha,
# chamar a próxima senha e desistir (encerrar o programa).
# Ao escolher a opção de criar nova senha, o programa gera uma nova senha,
# que será adicionada ao final de uma lista.
# Ao escolher a opção de chamar próxima senha, o programa deve remover e exibir a primeira senha da lista,
# simulando o atendimento em ordem de chegada. A opção de desistir encerra o programa.
# Após cada ação realizada, o programa deve exibir a lista atualizada de senhas.
# O funcionamento do programa deve manter a ordem das senhas conforme foram inseridas,
# garantindo que a primeira a ser chamada sempre seja a que entrou primeiro.

senhas = []

ultimo_numero = 0


while True:
    print("""
=========================
1. Criar nova senha
2. Chamar próxima senha
3. Sair do programa
=========================
    """)
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        ultimo_numero += 1  
        nova_senha = ultimo_numero
        senhas.append(nova_senha)
        print(f"✅ Senha {nova_senha} criada com sucesso!")
        print(f"   Senhas na fila: {senhas}")

    elif opcao == '2':
        if senhas:

            senha_chamada = senhas.pop(0)
            print(f" Chamando senha: {senha_chamada}")
            print(f"   Senhas restantes: {senhas}")
        else:
            print(" Nenhuma senha na fila para chamar.")

    elif opcao == '3':
        print("Programa encerrado.")
        break 

    else:
        print("X Opção inválida. Tente novamente.")