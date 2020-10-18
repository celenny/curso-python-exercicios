print('\033[0;31m''Ola, mundo')
nome = str(input('Qual seu nome:'))
print('\033[4;35m''Prazer em te conhecer {}'.format(nome))
a = 'luiz'
b = 'Rosário'
c = 'Joaquim'
print('Sei que sua mae se chama \033[:33m{} , seu pai \033[:34m{} e seu irmão \033[:32m{}'.format(b, c, a))
# Cores no terminal
''' códigodos de cores 
 \033[0:33:44m
 \033[STYLE:TEXT:BACKm'''
''' cores text/back
30/40 - branco
31/41 - vermelho
32/42 - verde
33/43 - amarelo
34/44 - azul
35/45 - roxo
36/46 - azul ciano
37/47 - cinza'''