from random import randint
from time import sleep
valores = list()


def sorteio(num):
    for c in range(1, num):
        valores.append(randint(1, 10))
    print('Soteando 5 valores da lista: ', end='')
    for v in valores:
        print(f'{v} ', end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def sompar(lista):
    soma = 0
    for v in valores:
        if v % 2 == 0:
            soma += v
    print(f'Somando os valores pares de {valores}, temos {soma}')


sorteio(6)
sompar(valores)
# funções para sortear e somar