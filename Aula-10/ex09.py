inicio = 0
seguinte = 1

for i in range (10):
    print(seguinte)
    proximo = inicio + seguinte
    inicio = seguinte
    seguinte = proximo