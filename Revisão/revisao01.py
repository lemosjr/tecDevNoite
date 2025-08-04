vendas = [941, 852, 783, 714, 697, 686, 685, 
670, 631, 453, 386, 371, 294, 269, 259]

vendedores = ['Maria','José', 'Antônio', 'João', 
'Francisco', 'Ana', 'Luiz',
'Paulo', 'Carlos', 'Fernanda', 'Juliana', 
'Sandro', 'Fábio', 'Tatiane', 'Célia']

bateu_meta = []
nao_bateu_meta = []


meta = 700
abaixo_meta = 500

for i in range(len(vendas)):
    if vendas[i] >= meta:
        bateu_meta.append(vendedores[i])
        
for i in range(len(vendas)):
    if vendas[i] < abaixo_meta:
        nao_bateu_meta.append(vendedores[i])

print(bateu_meta)
print(nao_bateu_meta)

