def criar_arquivo():
    with open('meu_arquivo.txt', 'w', encoding='utf-8') as arquivo:
        arquivo.write('Olá, este é meu novo arquivo\n')
        arquivo.write('Esta é a outra linha.\n')
    print("Arquivo 'meu_arquivo.txt' criado com sucesso (ou sobrescrito)!")

def ler_arquivo():
    with open('meu_arquivo.txt','r',encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
        print("TAMO JUNTOOOOOOO")

def modificar_arquivo():
    with open('meu_arquivo.txt','w', encoding='utf-8') as arquivo:
        arquivo.write(input("Digite a linha a ser adicionada:\n"))    
    ler_arquivo()
        
modificar_arquivo()

