soma = 0
while True:
    num = int(input("Digite o número a ser somado:"))
    soma = num + soma
    print(f"O valor somado é:{soma}")
    saida = input("Deseja sair s/n:")
    if saida == "s":
        break