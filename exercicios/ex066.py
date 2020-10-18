n = soma = 0
while True:
    n = int(input('Digite um numero:'))
    if n == 999:
        break
        soma += n
    print(f'A soma vale {soma}')
# comando flag (bandeira) ou condição de parada