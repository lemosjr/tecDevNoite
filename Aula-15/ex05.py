# . Faça um programa que simule um lançamento de dados.
# Lance o dado 100 vezes e armazene os resultados em uma Lista.
# Depois, mostre quantas vezes cada valor foi conseguido.
# Dica: use um listade contadores (1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.

import random
contadores = [0] * 6

for _ in range(100):
    resultado = random.randint(1, 6)
    contadores[resultado - 1] += 1

for i in range(6):
    print(f"Face {i + 1}: {contadores[i]} vezes")
    
