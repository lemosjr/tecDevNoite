num = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))
num3 = int(input("Digite o terceiro número:"))

print("Calculando o maior número...")

if num > num2 and num > num3:
    print(f'''
        O número maior é {num}      
          ''')
elif num2 > num and num2 > num3: 
    print(f'''
        O número maior é {num2}      
          ''')
else:
    print(f'''
        O número maior é {num2}      
          ''')