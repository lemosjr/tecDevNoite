# Questão 4: Adicione informações adicionais à pessoa no dicionário, como seu endereço de e-mail e número de telefone.

pessoa = {"nome":'junior', "idade":24, "cidade natal":{"rua":'tritao gonçalves', "cidade": 'fortaleza', "estado": 'CE'}, "profissao": 'dev-junior'}

pessoa['email'] = "joaopedro@gmail.com"
pessoa['numero'] = "85 988546365"

chaves = pessoa.keys()

print(chaves)
