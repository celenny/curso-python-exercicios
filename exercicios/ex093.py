player = {}
gol = list()
player['nome'] = str(input('Nome:'))
partidas = int(input(f'Quantas partidas {player["nome"]} jogou ?'))
for c in range(0, partidas):
    gol.append(int(input(f'     Quantos gols na partida {c} ?')))
player['gols'] = gol[:]
player['total'] = sum(gol)
print('-='*25)
print(player)
print('-='*25)
for k, v in player.items():
    print(f'O campo {k} tem valor {v}')
print('-='*25)
print(f'O jogador {player["nome"]} jogou {partidas} partidas.')
for p, v in enumerate(gol):
    print(f'   => Na partida {p}, fez {v} gols. ')
print(f'Com o total de {player["total"]} gols.')
# cadastro jogador dicionário