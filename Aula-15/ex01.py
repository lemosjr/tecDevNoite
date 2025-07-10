temperatura = []
tempAcima = []
media = 0
for i in range(3):
    temperatura.append(int(input("Digite uma temperatura:")))
    media = sum(temperatura) / len(temperatura)

print(temperatura)

for i in range(len(temperatura)):
    if i > media:
        tempAcima.append(i)
        
print(temperatura)
print(tempAcima)