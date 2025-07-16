# Questão 7 : Peça ao usuário para inserir o nome de um amigo e verifique se esse nome existe no dicionário de amigos.
amigos = {"levi":{"nome":'levi', "idade": 22}, "joao pedro":{"nome": 'joao pedro', "idade": 24}, "tales":{"nome": 'tales', "idade": 22}}

for nome, idade in amigos.items():
    amigo = input("Digite o nome do seu amigo:")
    if amigo in amigos:
        print(f"{amigo} está na lista")
    else:
        print(f"{amigo} não está na lista")
