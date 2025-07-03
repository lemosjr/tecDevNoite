# Questão 7: Faça um programa que receba dois números inteiros e 
# gere os números inteiros que estão no intervalo
# compreendido por eles

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

while True:
    if num1 < num2:
        for i in range(num1 + 1, num2):
            print(i)
        break
    elif num1 > num2:
        for i in range(num2 + 1, num1):
            print(i)
        break
    else:
        print("Os números são iguais. Tente novamente.")
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))