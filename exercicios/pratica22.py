def fatorial(n):
    f = 1
    for c in range(1, n + 1):
        f *= c
    return f


# programa principal
num = int(input('Você quer fatorial de ?'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')