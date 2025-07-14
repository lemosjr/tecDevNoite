# 7. Uma UBS possui um estoque de vacinas com os seguintes lotes (quantidades): [120, 85, 100, 50, 95].
# Crie um programa que remova o lote com menor quantidade e adicione um novo lote com 130 unidades. Mostre o estoque final.

lotes = [120, 85, 100, 50, 95]
lote_menor = min(lotes)
lotes.remove(lote_menor)
lotes.append(130)
print(lotes)