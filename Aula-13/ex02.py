#Escreva uma função chamada calcular_media que receba uma lista de números e retorne a média desses números.
def calcular_media():
    media = 0
    cNota = 0
    notas = int(input("Digite quantas notas serão somadas:"))
    for i in range(notas):
        if notas > 0:
            i += 1
            nota = float(input("Digite a nota:"))
            cNota += nota
            media = cNota / notas
        else:
            return print("Digite uma quantidade válida!")
    print(f"A média do aluno é {media}")
            
calcular_media()