# Questao 8: Faça um programa que peça um número inteiro 
# e determine se ele é ou não um número primo. 
# Um número primo é aquele que é divisível somente por ele mesmo e por 1.

num = int(input("Digite um número inteiro: "))

while True:
    if num % 2 == 0 and num != 2:
        print(f"{num} não é um número primo. tente novamente.")
        num = int(input("Digite um número inteiro: "))
    elif num < 2:
        print(f"{num} não é um número primo. tente novamente.")
        num = int(input("Digite um número inteiro: "))
    else:
        print(f"{num} é um número primo.")
        break
    