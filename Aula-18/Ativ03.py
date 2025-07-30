# Atividade 3: Classe Carro

#Crie uma classe chamada Carro com atributos marca e modelo.
#Adicione um método chamado descrever que imprime a marca e o modelo do carro.
#Crie dois objetos dessa classe e chame o método.
#Crie os métodos fechar_porta e metodo abri_porta.

class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.porta_aberta = False
        
    def descrever(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}"
    
    def fechar_porta(self):
        if self.porta_aberta:
            self.porta_aberta = False
            return "Porta fechada."
        else:
            return "A porta já está fechada."
    
    def abrir_porta(self):
        if not self.porta_aberta:
            self.porta_aberta = True
            return "Porta aberta."
        else:
            return "A porta já está aberta."
carro1 = Carro('Toyota', 'Corolla')
carro2 = Carro('Honda', 'Civic')
print(carro1.descrever())
print(carro2.descrever())
print(carro1.abrir_porta())
print(carro1.fechar_porta())
# Marca: Toyota, Modelo: Corolla
# Marca: Honda, Modelo: Civic
# Porta aberta.
# Porta fechada.
