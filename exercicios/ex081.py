values = list()
while True:
    values.append(int(input('Digite um valor:')))
    resp = ' '
    while resp not in 'snSN':
        resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*10)
print(f'Você digitou {len(values)} números')
values.sort(reverse=True)
print(f'Os valores em ordem decrescente são:{values}')
if 5 in values:
    print('O valor 5 faz parte da Lista ')
else:
    print('O valor 5 não faz parte da Lista')
# extraindo dado de uma lista
