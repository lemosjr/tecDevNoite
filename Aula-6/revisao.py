cargo = input("Digite seu cargo:")
msalario = 1518 
salario = 0

if cargo == "vendedor":
    salario = msalario 
elif cargo =="analista":
    aumento = msalario * 0.10
    salario = aumento + msalario
elif cargo == "gerente":
    aumento = msalario * 0.20
    salario = aumento + msalario
else:
    print("Informação inválida")

print(f'''
-------------Cargo-----------------
        Cargo:{cargo}
        Salário:R${salario:.2f}          
-----------------------------------
          ''')
