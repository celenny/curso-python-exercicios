def linha():
    print('-='*24)


def maior(*valores):
    for i, v in enumerate(valores):
        if i == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    linha()
    print(' Analisando os valores passados ...')
    print(f' {valores} foram informados {len(valores)} valores ao todo')
    print(f' O maior valor informado foi {maior}')


maior(2, 9, 4, 5)
maior(4, 7, 0)
maior(1, 2)
maior(1, 11, 24)
# função maior número :0