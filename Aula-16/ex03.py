# Questão 3: Modifique o valor de um item no dicionário que você criou e, em seguida, imprima o dicionário atualizado.
pessoa = {"nome":'junior', "idade":24, "cidade natal":{"rua":'tritao gonçalves', "cidade": 'fortaleza', "estado": 'CE'}, "profissao": 'dev-junior'}

print(pessoa)

chaves = pessoa.values()
pessoa["nome"] = "Joao pedro"
print(chaves)