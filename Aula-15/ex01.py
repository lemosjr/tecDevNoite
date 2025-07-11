lista = []
acimaDaMedia = []

for i in range(10):
    lista.append(int(input("Digite uma temperatura:")))
    
media = sum(lista) / len(lista)

for i in lista:
    if i > media:
        acimaDaMedia.append(i)

print(acimaDaMedia)

