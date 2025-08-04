# atv4
# Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura

# Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura += 0.5
        self.idade += 1

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg

    def crescer(self, cm):
        self.altura += cm
        
# Programa principal
nome = input("Informe o nome da pessoa: ")
idade = int(input("Informe a idade da pessoa: "))
peso = float(input("Informe o peso da pessoa (em kg): "))
altura = float(input("Informe a altura da pessoa (em cm): "))
pessoa = Pessoa(nome, idade, peso, altura)
print(f"Nome: {pessoa.nome}, Idade: {pessoa.idade}, Peso: {pessoa.peso} kg, Altura: {pessoa.altura} cm")
pessoa.envelhecer()
print(f"Após envelhecer, Idade: {pessoa.idade}, Altura: {pessoa.altura} cm")
pessoa.engordar(2)
print(f"Após engordar, Peso: {pessoa.peso} kg")
pessoa.emagrecer(1)
print(f"Após emagrecer, Peso: {pessoa.peso} kg")
pessoa.crescer(3)
print(f"Após crescer, Altura: {pessoa.altura} cm")
