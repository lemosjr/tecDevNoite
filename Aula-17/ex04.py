def caractere():
    with open('novo_arquivo.txt', 'r', encoding='utf-8') as arquivo_leitura:
        conteudo = arquivo_leitura.read()

    novo_conteudo = ""  # Cria uma nova string vazia para as modificações
    for letra in conteudo: # Não precisa do .lower() aqui se você for comparar as duas versões
        # Verifica tanto letras maiúsculas quanto minúsculas
        if letra.lower() in 'aeiouáéíóúãõ':
            novo_conteudo += '*' # Adiciona o asterisco
        else:
            novo_conteudo += letra # Adiciona a letra original se não for vogal
    
    with open('novo_arquivo.txt', 'w', encoding='utf-8') as arquivo_escrita:
        arquivo_escrita.write(novo_conteudo)

caractere()