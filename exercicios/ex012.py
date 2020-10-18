p = float(input('Qual o preço do produto? R$'))
d = p*0.05
np = p-d
print('O produto que custava R$ {}, com o cupom de 5% você ganha desconto de R${:.2f} ,'.format(p, d))
print('e seu produto agora passará a custar {:.2f}'.format(np))
