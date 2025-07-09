# lista_palavras = ["banana", "abacaxi", "laranja", "Uva", "maçã"]

# #Utilizando todas as funções de lista dentro do print

# print("Tamanho da lista", len(lista_palavras),
# "\n Lista de palavras:", lista_palavras,
# "\n Menor palavra (lexicograficamente)", min(lista_palavras),
# "\n Maior palavra(lexicograficamente)", max(lista_palavras),
# "\n Lista Ordenada:", sorted(lista_palavras))

####################### LISTAS #######################################

# lista = [1, 2, 3, 4, 5]

# # Adicionando elementos com .append(), .insert() e .extend()
# lista.append(6) # adiciona 6 ao final da lista
# print(lista)
# lista.insert(0, 0) # insere 0 na posição 0
# print(lista)
# lista.extend([7, 8, 9]) # adiciona os elementos 7, 8, 9 ao final da lista
# print(lista)
# # Removendo elementos com .remove(), .pop() e .clear()
# lista.remove(5) # remove o elemento 5
# print(lista)
# elemento_removido = lista.pop(2) # remove o elemento na posição 2 e retorna o valor removido
# print(lista)
# lista.clear() # limpa a lista completamente
# print(lista)

######################### LISTAS ########################################

# lista = [1,2,2,3,4,4,3,4,5]

# # Usando .index() para buscar o índice do primeiro elemento igual a 2
# print("Índice do primeiro '2' na lista:", lista.index(2))
# print(lista)

# # Usando .count() para contar quantas vezes o elemento 2 aparece na lista
# print("Número de vezes que '2' aparece na lista:", lista.count(2))
# print(lista)