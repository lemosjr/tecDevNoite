cont = 0
frase = input("Digite uma frase:")
letra = []
for letra in frase:
    if letra != " ":
        cont += 1
    print(letra)

print(f"Sua frase tem {cont} letras")