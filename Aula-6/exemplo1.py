idade = int(input("Digite sua idade:"))

if idade <= 18:
    print("Você é jovem")
elif idade > 18 and idade <= 65:
    print("Você é adulto")
else:
    print("Você é idoso") 