# Questão 6:  Crie um dicionário com informações sobre vários amigos. Use um loop para iterar pelos itens do dicionário e imprimir os nomes e idades dos amigos.

amigos = {"amigo1":{"nome":'levi', "idade": 22}, "amigo2":{"nome": 'joao pedro', "idade": 24}, "amigo3":{"nome": 'tales', "idade": 22}}

for nome,idade in amigos.items():
    print(nome,idade)