# Desafio 2:
# Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
# Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
par = []
impar = []
for i in lista:
    if lista[i] % 2 == 0: 
        lista[i] = par
    else:
        lista[i] = impar

print(par)
print(impar)
print(lista)