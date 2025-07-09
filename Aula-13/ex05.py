# Questão 5: Função para Verificar Palíndromo. 
# Escreva uma função chamada eh_palindromo que receba uma string e
# retorne True se a string for um palíndromo e False caso contrário.
# (Uma string é um palíndromo se lê da mesma forma de trás para frente.)
# Dica pesquise sobre conceito de slicing

def eh_palindromo(palavra):
    palavra = palavra.lower()          # deixa tudo em minúsculo
    #DICA: se fosse um franse podeiramos usar : replace(" ", "")

    #slicing 
    #Palavra[Inicio:Fim:passo]
    #início: onde começar (se vazio, começa do início).
    #fim: onde terminar (se vazio, vai até o fim).
    #passo: o tamanho do passo. Se for -1, anda de trás para frente.

    palavra_invertida = palavra[::-1]  # cria a string invertida
    return palavra == palavra_invertida  # compara original com invertida

while True:
    palavra = input("Escreva um paralavra para saber se é palindromo: ")
    if eh_palindromo(palavra):
        print("É palindromo")
    else:
        print("Não é palindromo")

