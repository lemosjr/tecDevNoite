# 3. Durante uma semana, foram registradas as temperaturas corporais de um paciente:
#                 [36.8, 37.5, 38.2, 37.0, 36.5, 39.1, 38.6]  
# Crie um programa que exiba apenas as temperaturas consideradas febre (acima de 37.5ºC).

temperaturas = [36.8, 37.5, 38.2, 37.0, 36.5, 39.1, 38.6]
febre = []

for temp in temperaturas:
    if temp > 37.5:
        febre.append(temp)

print("Temperaturas com febre:", febre)
