alunos = {}
alunos['nome'] = str(input('Nome:'))
alunos['média'] = float(input(f'Média do(a) {alunos["nome"]}:'))
if 5 <= alunos['média'] < 7:
    alunos['situaçao'] = 'Recuperação'
elif alunos['média'] >= 7:
    alunos['situaçao'] = 'Aprovado'
else:
    alunos['situaçao'] = 'Reprovado'
print('-='*15)
for k, v in alunos.items():
    print(f'- {k} é igual {v}')
print('-='*15)
# dicionário em python aprovação