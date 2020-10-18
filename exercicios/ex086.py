matrz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matrz[l][c] = int(input(f'Digite um valor para [{l},{c}]:'))
print('-='*11)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrz[l][c]:^5}]', end='')
    print()
# matriz em python 3x3