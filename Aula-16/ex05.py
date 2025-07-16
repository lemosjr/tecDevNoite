# Questão 5: Remova um item do dicionário, como o número de telefone, e imprima o dicionário atualizado.
pessoa = {"nome":'junior', "idade":24, "cidade natal":{"rua":'tritao gonçalves', "cidade": 'fortaleza', "estado": 'CE'}, "profissao": 'dev-junior'}

del pessoa["cidade natal"]

print(pessoa)