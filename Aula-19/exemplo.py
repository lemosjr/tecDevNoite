class Carro:
    rodas = 4
    volante = True
    cinto_seguranca = True
    estepe = True
    macaco = 1
    def __init__(self,ano,modelo):
        self.ano = ano
        self.modelo = modelo

carro1 = Carro(2020, "HB20")

print(carro1.ano)
print(carro1.modelo)
print(carro1.rodas)
print(carro1.volante)
print(carro1.cinto_seguranca)
print(carro1.estepe)
print(carro1.macaco)