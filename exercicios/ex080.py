num = []
for cont in range(0, 5):
    n = int(input('Digite um valor:'))
    if cont == 0 or n > num[-1]:
        num.append(n)
        print(f'Adicionando no final da lista...')
    else:
        pos = 0
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos, n)
                print(f'Adicionando na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados em ordem foram {num}')
# lista ordenada sem respetições

