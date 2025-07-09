# Questao 10 - Escreva uma função chamada contar_multiplos que recebe dois números inteiros: 
# limite e multiplo. A função deve retornar quantos números até o limite são divisíveis pelo multiplo.

def contar_multiplos(limite, multiplo):
    contador = 0
    for i in range(1, limite + 1):
        if i % multiplo == 0:
            contador += 1
    return contador
# Chamada da função e impressão do resultado
limite = int(input("Digite o limite: "))
multiplo = int(input("Digite o múltiplo: "))
resultado = contar_multiplos(limite, multiplo)
print(f"Quantidade de múltiplos de {multiplo} até {limite}: {resultado}")