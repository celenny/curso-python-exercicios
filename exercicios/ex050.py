# Soma dos numeros impares
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}° numero:'.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Voce informou {} numeros pares e a soma é a {}'.format(cont, soma))

