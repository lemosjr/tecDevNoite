# Desafio 2:
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

def preencher_lista(tamanho):
    lista = []
    for i in range(tamanho):
        lista.append(i)
    return lista

def dividir_lista(lista):
    par = []
    impar = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            par.append(lista[i])
        else:
            impar.append(lista[i])
    return par, impar


def main():
    tamanho = int(input("Digite o tamanho da lista: "))
    lista = preencher_lista(tamanho)
    par, impar = dividir_lista(lista)
    print("Lista par: ", par)
    print("Lista impar: ", impar)

main()