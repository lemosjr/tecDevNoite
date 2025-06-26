vtotal = 0
menu = int(input(f'''
-------------lanches------------
|    1 - Hamburguer 7.00$      |
|    2 - Bauru   8.00$         |
|    3 - Coxinha 5.00$         |
|                              |
--------------------------------\n
Entrada:'''))

if menu == 1:
    preco = 7
    quant = int(input("Quantidade:"))
elif menu == 2:
    preco = 8
    quant = int(input("Quantidade:"))
elif menu == 3:
    preco = 5
    quant = int(input("Quantidade:")) 
else:
    print("Digite uma entrada válida!!!")
    
vtotal = preco * quant
print(f"O valor total a ser pago é R${vtotal:.2f}")