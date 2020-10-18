def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}X{c} é {a}m²')
    print('-=' * 20)


# programa principal
print('-='*20)
print('       Calculadora de Áreas       ')
print('-=' * 20)
larg = float(input('LARGURA (m):'))
comp = float(input('COMPRIMENTO (m):'))
area(larg, comp)
