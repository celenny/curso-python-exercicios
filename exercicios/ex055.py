maior = menor = 0
# maior e menor sequencia
for p in range(1, 6):
    peso = float(input(('Peso da {}° pessoa (kg):'.format(p))))
    if p == 1:
       maior = peso
       menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O Maior peso lido foi {} kg'.format(maior))
print('O Menor peso lido foi {} kg'.format(menor))
