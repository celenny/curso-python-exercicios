print('-=-' * 10)
print('Sequência de Fibonacci')
print('-=-' * 10)
limit = int(input('Quantos termos você quer mostrar ?'))
x = 1
y = 0
cont = 0
while cont != limit:
    z = x + y
    x = y
    y = z
    print('{}'.format(z), end='')
    print(' ➔ ' if cont != limit else '', end='')
    cont += 1
print('FIM')
# Sequencia fibonacci versão 1.0