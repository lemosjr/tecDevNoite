total = 0
numeros = int(input("Digite quantos números você quer somar:"))
for i in range(numeros):
    numero = int(input("Digite o número:"))
    total += numero

print(f"A soma dos numeros é {total}")