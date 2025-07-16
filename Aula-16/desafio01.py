# Desafio-1
# Crie um dicionário de tradução que mapeie palavras de um idioma para outro (por exemplo, inglês para espanhol).
# Peça ao usuário para inserir uma palavra em inglês e, em seguida, imprima a tradução correspondente.

dicionario_traducao = {
    "hello": "hola",
    "goodbye": "adiós",
    "please": "por favor",
    "thank you": "gracias"
}

def significado():
    palavraSig = input("Digite o signifcado da palavra:")
    for palavraSig in dicionario_traducao.values():
        for chave, valor in dicionario_traducao.items():
            if valor == palavraSig:
                return print(chave)
            
        
            
def inserir_palavra():
    palavraNova = input("Digite a nova palavra:")
    traducao = input("Digite a tradução da palavra digitada:")
    dicionario_traducao[palavraNova] = traducao



def tradutor():
    palavra_ingles = input("Digite uma palavra em inglês: ")

    if palavra_ingles in dicionario_traducao:
        print("A tradução em espanhol é:", dicionario_traducao[palavra_ingles])
    else:
        print("Palavra não encontrada no dicionário.")

significado()
