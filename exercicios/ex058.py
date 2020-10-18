from random import randint
computer = randint(0, 10)
c = 1
print('Sou seu Computador e te desafio em um jogo de adivinhação.')
print('Pensei em um numero entre 0 e 10 .')
print('Você consegue adivinhar ?')
player = int(input('Qual é seu palpite ?'))
while player != computer:
    if player < computer:
        print('Mais ... tente novamente')
    elif player > computer:
        print('Menos ... tente novamente')
    player = int(input('Qual é o seu palpite ?'))
    c += 1
print('Depois de {} tentativas. PARABÉNS !'.format(c))
# Jogo De Adivinhação versão 2.0