impar = 0
cont = 0
num = int(input("Digite quantos números serão contados:"))
while True:
    if cont < num:
        cont = cont + 1
    else:
        break
    if cont % 2 != 0 :
        impar += 1
        print(f"Numeros impares:{cont}")
print(f"Existem {impar} números impares")
    