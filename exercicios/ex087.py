matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somter = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
        if matrix[l][c] % 2 == 0:
            soma += matrix[l][c]
        if matrix[l][2]:
            somter += matrix[l][2]
print('-='*14)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
print('-='*14)
print(f'A soma dos valores pares é {soma}')
print(f'Soma dos valores da 3° coluna : {somter}')
print(f'O maior valor da 2° linha é {max(matrix[1])}')



