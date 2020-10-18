from random import randint
print('Vamos Jogar PAR ou IMPAR')
print('-='*15)
v = 0
while True:
    player = int(input('Digite um valor :'))
    computer = randint(0, 10)
    total = player + computer
    tipo = ''
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar ? [P/I]')).strip().upper()[0]
        print(f'Voce jogou {player} e o computador {computer}.Total de {total}')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você VENCEU !')
                v += 1
            else:
                print('Você PERDEU !')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você VENCEU !')
                v += 1
            else:
                print('Você PERDEU !')
                break
        print('Vamos Jogar Novamente ...')
print(f'GAME OVER ! Você Venceu {v} vezes')
