# Questao 9 - Escreva uma função chamada falar_como_robo que receba uma frase 
# e retorne a mesma frase com todas as letras em maiúsculo e separadas por hífens.

def falar_como_robo():
    frase = input("Digite uma frase: ")
    # Converte a frase para maiúsculas e separa as letras por hífens
    frase_robo = '-'.join(frase.upper())
    return frase_robo

# Chamada da função e impressão do resultado
resultado = falar_como_robo()
print(resultado)

    