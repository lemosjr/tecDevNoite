num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if num1 >= num2 and num1 >= num3:
    primeiro = num1
    if num2 >= num3:
        segundo = num2
        terceiro = num3
    else:
        segundo = num3
        terceiro = num2
elif num2 >= num1 and num2 >= num3:
    primeiro = num2
    if num1 >= num3:
        segundo = num1
        terceiro = num3
    else:
        segundo = num3
        terceiro = num1
else:
    primeiro = num3
    if num1 >= num2:
        segundo = num1
        terceiro = num2
    else:
        segundo = num2
        terceiro = num1
        
print(f"A ordem decrescente do números é {terceiro}, {segundo} e {primeiro}")