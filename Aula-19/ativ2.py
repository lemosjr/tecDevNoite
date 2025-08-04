# atv2
# Classe Quadrado: Crie uma classe que modele um quadrado:

# Atributos: Tamanho do lado

# Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;


class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def retornarLado(self):
        return self.lado

    def calcularArea(self):
        return self.lado ** 2
    
quadrado1 = Quadrado(5)
quadrado1.mudarLado(10)
print(quadrado1.retornarLado())
print(quadrado1.calcularArea())
