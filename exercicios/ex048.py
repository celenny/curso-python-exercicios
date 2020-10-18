quant = 0
soma = 0
for cont in range(1, 501, 2):
    if cont % 2 != 0 and cont % 3 == 0:
        quant += 1
        soma += cont
print('A soma dos {} valores é igual a {}'.format(quant, soma))
''' soma tds os valores ímpares de 1 à 500 que sejam múltiplos de 3 '''