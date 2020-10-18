numbers = []
even = []
odd = []
while True:
    numbers.append(int(input('Digite um número:')))
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(numbers):
    if v % 2 == 0:
        even.append(v)
    else:
        odd.append(v)
print('-='*10)
print(f'Lista completa:{numbers}')
print(f'Pares:{even}')
print(f'Ímpares:{odd}')
# dividindo valores em varias listas