# Atividade 2: Criando e Usando uma Classe

#     Crie uma classe chamada Livro com atributos titulo e autor. Adicione um método chamado detalhes
#     que imprime o título e o autor do livro. Crie um objeto dessa classe e chame o método.
#     Crie o método reputação,no qual fala qual a reputação do livro

class Livro:
    def __init__(self, titulo, autor, reputacao):
        self.titulo = titulo
        self.autor = autor
        self.reputacao = reputacao
        
    def detalhes(self):
        return f"Título: {self.titulo}, Autor: {self.autor}"
    
    def reputacao(self):
        if self.reputacao >= 4.5:
            return "Livro excelente"
        elif self.reputacao >= 3.0:
            return "Livro bom"
        else:
            return "Livro regular"
livro = Livro('Dom Casmurro', 'Machado de Assis', 4.7)
print(livro.detalhes())
print(livro.reputacao())

# Livro: Dom Casmurro, Autor: Machado de Assis
# Livro excelente