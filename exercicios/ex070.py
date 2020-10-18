print('  LOJÃO BURITI ')
soma = more1000 = quant = 0
barato = ' '
while True:
    product = str(input('Nome do Produto:'))
    price = float(input('Preço: R$'))
    soma += price
    quant += 1
    if price > 1000:
        more1000 += 1
    if quant == 1 or price < menor:
        menor = price
        barato = product
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${soma:.2f}')
print(f'Temos {more1000} produtos com preço acima de R$1000.00')
print(f'O pruduto mais barato foi {barato} custando R${menor}')
