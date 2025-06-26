num = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

if (num >= num2 and num >= num3) and (num2 >= num3):
    print(f"Ordem decrescente {num3}, {num2} e {num}")
elif (num2 >= num and num2 >= num3) and (num >= num3):
    print(f"Ordem decrescente {num2}, {num} e {num3}")
else:
    print(f"Ordem decrescente {num}, {num2} e {num3}")