from aluno.aluno import Aluno
alunos = []
print("-"*30)
print("Sistema de gerenciamento de alunos")

while True:
    print("-"*30)
    print("1 - Cadastrar aluno")
    print("2 - Exibir Dados")
    print("0 - Sair")
    opcao = input("Entrada:")
    
    if opcao == '1':
        nome = input("Nome do aluno:")
        matricula = input("Matricula:")
        curso = input("curso:")
        novo_aluno = Aluno(nome, matricula, curso)
        alunos.append(novo_aluno)
    elif opcao == '2':
        for i, aluno in enumerate(alunos):
            print(f"ID: {i+1} | Nome: {aluno.nome} | Curso: {aluno.curso}")
        
        try:
            escolha = int(input("Digite o número do aluno que deseja visualizar os detalhes:")) - 1
            
            if 0 <= escolha < len(alunos):
                aluno_selecionado = alunos[escolha]
                print("--- Detalhes do Aluno ---")
                print(f"Nome: {aluno_selecionado.nome}")
                print(f"Matrícula: {aluno_selecionado.matricula}")
                print(f"Curso: {aluno_selecionado.curso}")
            else:
                print("Aluno não encontrado ou número inválido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")