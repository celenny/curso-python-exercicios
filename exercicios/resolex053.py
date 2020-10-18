frase = str(input('Digite uma frase:')).strip().upper()
divisão = frase.split()
junção = ''.join(divisão)
inverso = ''
for letra in range(len(junção) - 1, -1, -1):
    inverso += junção[letra]
print('O inverso de {} é {}'.format(junção, inverso))
if inverso == junção:
    print('Temos um palíndromo')
else:
    print('A frase digittada não é um palíndromo. ')
# feito pelo professor gustavo guanabara
