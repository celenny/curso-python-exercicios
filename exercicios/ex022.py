nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome ...')
print('Em maiusculas temos {}'.format(nome.upper()))
print('Em minusculas {}'.format(nome.lower()))
print('Quntidade de caracteres é {}'.format(len(nome) - nome.count(' ')))
print('Seu Primeiro nome tem {} letras '.format(nome.find(' ')))


