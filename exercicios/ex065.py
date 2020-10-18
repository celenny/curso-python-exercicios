resp = 'S'
soma = quant = 0
while resp != 'N':
    n = int(input('Digite um numero: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar ? [S/N]')).upper().strip()[0]
media = soma/quant
print('Você digitou {} números e a média foi {:.1f}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
# Analisando valores (media , menor e maior numero)
