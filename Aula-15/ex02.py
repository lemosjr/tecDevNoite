lista = []

for i in range(20):
    menu = int(input(f'''
    1 - criar nova senha
    2 - chamar senha
    3 - sair
Entrada:'''))
    if menu == 1:
        lista.append(i)
    elif menu == 2:
        print(lista[i])
        lista.pop()
    elif menu == 3:
        print("Encerrando programa...")
        break
    else:
        print("Digite uma entrada válida")