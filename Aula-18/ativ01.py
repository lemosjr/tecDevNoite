# Atividade 1: Criação de uma Classe e Objeto
#     Crie uma classe chamada Aluno com atributos nome e matricula. Adicione um método chamado
#     exibir_informacoes que imprime os detalhes do aluno. Crie um objeto dessa classe e chame o método. Crie o
#     método aprovado_reprovado que verifica se o aluno foi ou não aprovado.

class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota
        
    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}"
    
    def aprovado_reprovado(self):
        if self.nota >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"
aluno = Aluno('João Silva', '123456', 7.5)
print(aluno.exibir_informacoes())
print(aluno.aprovado_reprovado())
# Nome: João Silva, Matrícula: 123456
# Aprovado