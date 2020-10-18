from random import randint
computer = randint(0, 5)
print('==-=='*12)
print('Vou pensar em um numero entre 0 e 5 te desafio a adivinhar')
print('==-=='*12)
player = int(input('Em que numero eu pensei :'))
print('processando ...')
if computer == player:
    print('WOW PARABENS ! Você conseguiu me VENCER !')
else:
   print('GANHEI! Eu pensei no numero {} e não no {}'.format(computer, player))
# Jogo De Adivinhação versão 1.0

