# Desafio 1:
# Crie uma lista de números inteiros e implemente uma código que substitua todos os números pares por 0

def substituir_numero(lista):
    for i in range(len(lista)):
        if lista [i] % 2 == 0:
            lista[i] = 0
    return lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(substituir_numero(lista))