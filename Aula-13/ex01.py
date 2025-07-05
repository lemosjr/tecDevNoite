def numeroPrimo(num):
    if num % 2 == 0 and num != 2:
       return print(f"{num} não é primo")
    else:
       return print(f"{num} é primo")

numeroPrimo(int(input("Digite um número inteiro:")))