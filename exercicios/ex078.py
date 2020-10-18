numeros = list()
menor = maior = 0
for n in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a posição {n}:')))
    if n == 0:
        maior = menor = numeros[n]
    else:
        if numeros[n] > maior:
            maior = numeros[n]
        if numeros[n] < menor:
            menor = numeros[n]
print('-='*20)
print(f'Você digitou os valores {numeros}')
print(f'O maior valor digitado foi {maior} na posições ', end='')
for i, v in enumerate(numeros):
    if v == maior:
        print(f'{i}..', end='')
print()
print(f'O menor valor digitdo foi {menor} na posições ', end='')
for i, v in enumerate(numeros):
    if v == menor:
        print(f'{i}..', end='')
print()
# maior e menor em LISTAS []