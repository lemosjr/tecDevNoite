# Questao 7 - Escreva uma função chamada contar_maiusculas que receba uma string 
# e retorne quantas letras maiúsculas existem nela.

def contar_maiusculas():
    while True:
        maiscula = 0
        frase = input("Digite uma frase:")
        for letra in frase:
            if letra.isupper():
                maiscula += 1
        print(f"Sua frase tem {maiscula} letras maisculuas")


contar_maiusculas()
