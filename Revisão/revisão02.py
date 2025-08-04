def somar_valor():
    print("Mercadinho BigBom")
    valor = 0
    while True:
        opcao = float(input(f"Digite o valor do produto:R$"))
        if opcao != 0 : 
            valor += opcao 
            print(valor)
        else:
            break
    return valor
def troco_cliente(valor):
    dinheiro = float(input("Valor pago pelo cliente:R$"))
    troco = dinheiro - valor
    return print(f"O troco do cliente é R${troco}")

def calcular_valor_final(valor):
    print(f"Preço a pagar:R${valor:.2f}") 

def main():
    while True:
        valor = somar_valor()
        calcular_valor_final(valor)
        troco_cliente(valor)
        continuar = input("Deseja continuar? s/n ")
        if continuar == "s":
            valor = somar_valor()
            calcular_valor_final(valor)
            troco_cliente(valor)
        else:
            break

main()  
        
        
        
    