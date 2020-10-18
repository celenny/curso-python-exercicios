dados = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('1° nota:'))
    n2 = float(input('2° nota:'))
    media = (n1 + n2)/2
    dados.append([nome, [n1, n2], media])
    resp = ' '
    resp = str(input('Quer continuar ?[S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*20)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*24)
for i, a in enumerate(dados):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*24)
    opc = int(input('Ver as notas de qual aluno ?[999 interrompe]'))
    if opc == 999:
        break
        print(' FINALIZANDO ...')
    if opc <= len(dados) - 1:
        print(f'As notas de {dados[opc][0]} são {dados[opc][1]}')
print('<< VOLTE SEMPRE >>')
# boletim com listas compostas


