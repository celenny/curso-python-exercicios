from random import randint
from time import sleep
from operator import itemgetter
dado = {'player1': randint(1, 6),
        'player2': randint(1, 6),
        'player3': randint(1, 6),
        'player4': randint(1, 6)}
ranking = list()
print('Valores sorteados :')
for k, v in dado.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('<'*5, f'RANKING', '>'*5)
for i, v in enumerate(ranking):
    print(f'- {i+1}º Lugar : {v[0]} com {v[1]}')
    sleep(1)