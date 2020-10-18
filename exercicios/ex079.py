values = []
while True:
    v = int(input('Digite um valor:'))
    if v not in values:
        values.append(v)
        print('valor adicionado com sucesso ...')
    else:
        print('valor duplucado ! não vou adicionar ...')
    resp = ' '
    resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*25)
values.sort()
print(f'Você digitou os valores {values}')
# valores únicos em lista