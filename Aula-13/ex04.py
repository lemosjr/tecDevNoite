# Questão 4: Faça um programa, com uma função que necessite de 
# Três argumentos, e que forneça a soma desses três argumentos.

def argumentos():
    soma = 0
    arg = int(input("Digite quantos números:"))
    for i in range(arg):
        i += 1
        arg1 = int(input("Digite um número:"))
        soma = arg1 + soma
        print(soma)
        
argumentos()