class Carro:
    def __init__(self, marca, ano, modelo, placa):
        self.marca = marca
        self.ano = ano
        self.modelo = modelo
        self.placa = placa
    
    def __str__(self):
        return f"""
        informações do carro
        
        Marca : {self.marca}
        Ano : {self.ano}
        Modelo : {self.modelo}
        placa : {self.placa}
    """
    
    