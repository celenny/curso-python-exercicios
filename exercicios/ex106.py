def  ajuda(msg):
    help(msg)


def title(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# programa principal
comando = ''
while True:
    title('SISTEMA DE AJUDA PyHELP')
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
title('VOLTE SEMPRE E ATÉ LOGO')