# Questao 9: Numa eleição existem três candidatos. 
# Faça um programa que peça o número total de eleitores. 
# Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 1
candidato2 = 2
candidato3 = 3

while True:
    eleitores = int(input("Digite o número total de eleitores: "))
    if eleitores <= 0:
        print("O número de eleitores deve ser maior que zero. Tente novamente.")
        eleitores = int(input("Digite o número total de eleitores: "))
    elif eleitores > 0:
        votos_candidato1 = 0
        votos_candidato2 = 0
        votos_candidato3 = 0
        
        for i in range(eleitores):
            voto = int(input(f"Eleitor {i + 1}, digite seu voto (1, 2 ou 3): "))
            while voto not in (candidato1, candidato2, candidato3):
                print("Voto inválido. Tente novamente.")
                voto = int(input(f"Eleitor {i + 1}, digite seu voto (1, 2 ou 3): "))
            
            if voto == candidato1:
                votos_candidato1 += 1
            elif voto == candidato2:
                votos_candidato2 += 1
            elif voto == candidato3:
                votos_candidato3 += 1
        
        print(f"Votos do Candidato 1: {votos_candidato1}")
        print(f"Votos do Candidato 2: {votos_candidato2}")
        print(f"Votos do Candidato 3: {votos_candidato3}")
        break
