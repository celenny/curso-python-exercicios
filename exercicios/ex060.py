num = int(input('calcular o fatorial:'))
c = num
f = 1
print('{}! = '.format(num), end='')
while c != 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f = f * c
    c -= 1
print('{}'.format(f))
print('-=' * 20)
