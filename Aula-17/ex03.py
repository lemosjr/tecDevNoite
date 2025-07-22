def caractere():
    with open('novo_arquivo.txt', 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        cont = 0
        for letra in conteudo.lower():
            if letra in 'o':
                cont += 1
                print(f"Letras E:{cont}")
                
caractere()
        