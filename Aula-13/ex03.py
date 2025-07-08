#Questão 3: Escreva uma função chamada contar_vogais que receba 
#Uma string e retorne o número de vogais (a, e, i, o, u) na string.

def contarVogais():
    cVogal = 0
    palavra = input("Digite uma palavra:")
    for letra in palavra:       
        if letra in "aeiou":
            cVogal += 1
        elif letra != "aeiou":
            continue
    print(f"Sua palavra possui {cVogal} vogais")
contarVogais()