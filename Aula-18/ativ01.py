# Atividade 1: Criação de uma Classe e Objeto
#     Crie uma classe chamada Aluno com atributos nome e matricula. Adicione um método chamado
#     exibir_informacoes que imprime os detalhes do aluno. Crie um objeto dessa classe e chame o método. Crie o
#     método aprovado_reprovado que verifica se o aluno foi ou não aprovado.

class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        
    def __str__(self):
        return f"{self.nome} - {self.matricula}"      
    
    def notas_do_aluno(self):
        if self.nota >=7 and self.nota<=10:
            return "Aluno aprovado"
        elif self.nota < 7 and self.nota >= 0:
            return "Aluno reprovado"
        else:
            return "Nota inválida"
aluno = Aluno('henrique', 245, 8.5)     
print(aluno)
print(aluno.notas_do_aluno())