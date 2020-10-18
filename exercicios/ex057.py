sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()[0]
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Informe o sexo novamente :')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))
# analisador de dados