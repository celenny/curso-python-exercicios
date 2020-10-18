def ficha(name='<descolhecido>', gol=0):
    print(f'O jogador {name} fez {gol} gol(s) no campeonato')


# programa principal
print('-='*24)
n = str(input('Nome do Jogador:'))
g = str(input('Números de Gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)
print('-='*24)

