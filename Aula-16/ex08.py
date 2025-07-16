# Questão 8: Conte quantos amigos existem no dicionário e imprima o resultado.

amigos = {"levi":{"nome":'levi', "idade": 22}, "joao pedro":{"nome": 'joao pedro', "idade": 24}, "tales":{"nome": 'tales', "idade": 22}}

for nome in amigos.items():
    chaves = amigos.keys()
    print(nome.count(chaves))