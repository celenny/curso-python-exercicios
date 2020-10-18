val = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
val[10] = 11
#val.sort(reverse=True)
val.insert(2, 3)
if 12 in val:
    val.remove(12)
else:
    print('Não encontrei o numero 12 na lista ')
print(val)
print(f'essa lista tem {len(val)} elementos')
# aulas de Listas [] parte 1