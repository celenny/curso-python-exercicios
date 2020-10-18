from random import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('-=-' * 13)
print('PEDRA -=- PAPEL -=- TESOURA')
print(''' Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
print('-=-' * 13)
jogador = int(input('Qual a sua jogada ?'))
print('Computador jogou {}'.format(itens[computador]))
print('Jogador escolheu {}'.format(itens[jogador]))
print('-=-' * 13)
if computador == 0: # computador joga pedra
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador VENCEU !')
    elif jogador == 2:
        print('Computador VENCEU !')
    else:
        print('Jogada INVÁLIDA')
elif computador == 1:  # computador joga papel
    if jogador == 0:
        print('Computador VENCEU !')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('Jogador VENCEU !')
    else:
        print('Jogada INVÁLIDA')
elif computador == 2:  # computador jogou tesoura
    if jogador == 0:
        print('Jogador VENCEU !')
    elif jogador == 1:
        print('Computador VENCEU !')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Jogada INVÁLIDA')
print('-=-' * 13)
