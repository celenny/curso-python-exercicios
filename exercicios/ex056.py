imenor = imaior = totidade = media = 0
vnome = ''
for p in range(1, 5):
    print('----- {}° PESSOA -----'.format(p))
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).upper()
    totidade += idade
    if sexo == 'F':
        if idade < 20:
            imenor += 1
    if sexo == 'M':
        if idade > imaior:
            imaior = idade
            vnome = nome
media = totidade/4
print('A media de idade do grupo foi {:.2f} anos'.format(media))
print('Ao todo temos {} mulheres com menos de 20 anos.'.format(imenor))
print('O homem mais velho tem {} anos e se chama {}'.format(imaior, vnome))
# Analisador de dados completo
