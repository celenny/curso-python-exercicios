frase = str(input('Digite uma frase:')).strip().upper()
inverso = frase[::-1]
print('O inverso de {} é {}'.format(frase, inverso))
if frase == inverso:
    print('Temos um palíndromo !')
else:
    print('A frase digitada não é um palíndromo.')
''' minha versão do ex 053 de palíndromo no outro 
arquivo temos a resolução do professor guanabara '''
