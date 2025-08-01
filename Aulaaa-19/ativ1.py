# atv1
# Classe Bola: Crie uma classe que modele uma bola:

# Atributos: Cor, circunferência, material

# Métodos: trocaCor, mostraCor e CalcArea


class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, nova_cor):
        self.cor = nova_cor

    def mostraCor(self):
        return self.cor

    def calcularArea(self):
        from math import pi
        raio = self.circunferencia / (2 * pi)
        return 4 * pi * (raio ** 2) 
    

bola1 = Bola("Azul", 75, "Couro")
bola1.trocaCor("Laranja")
print(bola1.mostraCor())
print(bola1.calcularArea())
