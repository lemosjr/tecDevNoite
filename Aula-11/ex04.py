while True:
    operacao = input("Digite a operação desejada (+, -, *, /) ou 'sair' para encerrar: ")
    num = float(input("Digite um número:"))
    num2 = float(input("Digite outro número:"))
    
    if operacao == 'sair':
        print("Encerrando o programa.")
        break
    
    if operacao == '+':
        resultado = num + num2
    elif operacao == '-':
        resultado = num - num2
    elif operacao == '*':
        resultado = num * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num / num2
        else:
            print("Erro: Divisão por zero não é permitida.")
            continue
    else:
        print("Operação inválida. Tente novamente.")
        continue
    
    print(f"O resultado da operação {num} {operacao} {num2} é: {resultado}")
    