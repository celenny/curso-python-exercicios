# Tabuada versão 2.0
num = int(input('Digite um numero para ver a sua Tabuada:'))
print('-=-'*12)
for c in range(1, 11):
    result = c*num
    print('{} x {} = {}'.format(c, num, result))
print('-=-'*4)
''' se voce quaser não é obrigado fazer uma variavel par mostrar o resultado 
basta apenas botar (c, num, c*num)'''

