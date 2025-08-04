# atv3
# Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)

# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o
# local.

class Retangulo:
    def __init__(self, lado_a, lado_b):
        self.lado_a = lado_a
        self.lado_b = lado_b

    def mudarLados(self, novo_lado_a, novo_lado_b):
        self.lado_a = novo_lado_a
        self.lado_b = novo_lado_b

    def retornarLados(self):
        return self.lado_a, self.lado_b

    def calcularArea(self):
        return self.lado_a * self.lado_b

    def calcularPerimetro(self):
        return 2 * (self.lado_a + self.lado_b)
    
# Programa principal
lado_a = float(input("Informe o comprimento do lado A: "))
lado_b = float(input("Informe o comprimento do lado B: "))  
retangulo = Retangulo(lado_a, lado_b)
print(f"Lados do retângulo: {retangulo.retornarLados()}")
print(f"Área do retângulo: {retangulo.calcularArea()}")
print(f"Perímetro do retângulo: {retangulo.calcularPerimetro()}")

# Calcular quantidade de pisos e rodapés
area_piso = float(input("Informe a área de um piso (em m²): "))
area_rodape = float(input("Informe a área de um rodapé (em m²): "))
quantidade_pisos = retangulo.calcularArea() / area_piso
quantidade_rodapes = retangulo.calcularPerimetro() / area_rodape
print(f"Quantidade de pisos necessários: {quantidade_pisos}")
print(f"Quantidade de rodapés necessários: {quantidade_rodapes}")