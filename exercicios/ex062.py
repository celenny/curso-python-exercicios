print('Gerador de P.A')
print('=-=' * 10)
primeiro = int(input('Primeiro termo:'))
razao = int(input('Razão da P.A:'))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} → '.format(termo),  end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer ver a mais :'))
print('Processando finalizada com {} termos mostrados'.format(total))
# versão P.A 3.0
