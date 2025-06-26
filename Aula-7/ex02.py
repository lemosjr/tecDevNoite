menu = int(input(f'''
--------------Menu--------------
|    1 - cadastrar vendedor    |
|    2 - cadastro de gerente   |
|    3 - cadastro de cliente   |
|                              |
--------------------------------\n
Entrada:'''))

if menu == 1:
    cpf = input("Digite o cpf:")
    idade = int(input("Digite idade:"))
    cidade = input("Digite cidade:")
    sal = float(input("Digite o salário:"))
    print(f'''
          Usuário:{cpf}
          cadastrado com sucesso...
          ''')
elif menu == 2:
    cpf2 = input("Digite o cpf:")
    idade2 = int(input("Digite idade:"))
    cidade2 = input("Digite cidade:")
    sal2 = float(input("Digite o salário:"))
elif menu == 3:
    cpf3 = input("Digite o cpf:")
    idade3 = int(input("Digite idade:"))
    cidade3 = input("Digite cidade:")
    sal3 = float(input("Digite o salário:"))
else:
    print("Entrada inválida")