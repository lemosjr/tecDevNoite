class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    
    def adicionar_estoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade inválida")
            return
        else:
            self.quantidade += self.quantidade 
    
    def remover_estoque(self, quantidade):
        if quantidade < 0:
            print("Quantidade inválida")
            return "Error"
        else:
            self.quantidade -= quantidade
    
            
    