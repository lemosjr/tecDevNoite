# Questao 8 - Escreva uma função chamada idade_em_meses que receba a idade de uma pessoa em anos 
# e retorne quantos meses de vida ela já teve (desconsidere dias ou anos bissextos).

def idade_em_meses():
    idade = int(input("Digite sua idade:"))
    idadeMes =  idade * 12
    print(f"Você teve {idadeMes} meses de vida")

idade_em_meses()