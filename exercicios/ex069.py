sexom = imenor20 = imaior18 = 0
while True:
    print('-'*25)
    print(' CADRASTRE UMA PESSOA ')
    print('-'*25)
    idade = int(input('Idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        imaior18 += 1
    if sexo == 'F' and idade < 20:
           imenor20 += 1
    if sexo == 'M':
        sexom += 1
    print('-'*25)
    resp = ' '
    while resp not in'SN':
        resp = str(input('Quer continuar ? [S/N]')).strip().upper()[0]
    if resp == 'N':
       break
print(f'Total de pessoas com mais de 18 anos :{imaior18}')
print(f'Ao todo temos {sexom} homens cadastrados')
print(f'E {imenor20} mulheres com menos de 20 anos.')
# Análise de dados do Grupo
