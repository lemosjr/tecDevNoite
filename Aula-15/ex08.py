# 8. Crie um programa para gerenciar os pedidos de uma lanchonete.
# O sistema deve simular um menu onde o atendente pode escolher entre as seguintes opções: 
# adicionar um novo pedido, visualizar todos os pedidos ou finalizar o pedido mais antigo.
# Ao escolher “adicionar pedido”, o atendente deve digitar o nome do cliente junto com o item solicitado 
# (por exemplo: "Ana - X-Burguer"), e essa informação deve ser adicionada à lista de pedidos.
# Ao escolher “visualizar pedidos”, o programa deve exibir todos os pedidos em ordem, da entrada mais antiga à mais recente.
# Já ao escolher “finalizar pedido”, o programa deve remover o primeiro item da lista, simulando que esse pedido foi atendido,
# e exibir qual foi o pedido finalizado. Após cada ação, o programa deve mostrar o estado atualizado da fila de pedidos.
# O sistema deve continuar funcionando até que o atendente escolha a opção de sair do programa.

pedidos = []
while True:
    print("""=========================
1. Adicionar novo pedido
2. Visualizar todos os pedidos
3. Finalizar pedido mais antigo
4. Sair
=========================
Escolha uma opção:""")
    opcao = input()

    if opcao == "1":
        pedido = input("Digite o nome do cliente e o item solicitado: ")
        pedidos.append(pedido)
        print(f"Pedido adicionado: {pedido}")

    elif opcao == "2":
        print("Lista de pedidos:")
        for p in pedidos:
            print(f" - {p}")

    elif opcao == "3":
        if pedidos:
            pedido_finalizado = pedidos.pop(0)
            print(f"Pedido finalizado: {pedido_finalizado}")
        else:
            print("Não há pedidos para finalizar.")

    elif opcao == "4":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")

    print("Estado atual da fila de pedidos:")
    for p in pedidos:
        print(f" - {p}")