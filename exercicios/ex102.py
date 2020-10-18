def fatorial(num=1, show=False):
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')

        f *= c
    return f


print('-='*20)
n = int(input('Digite um número:'))
print(fatorial(n, show=True))
print('-='*20)
# função fatorial 
