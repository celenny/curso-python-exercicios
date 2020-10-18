n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))
media = (n1 + n2)/2
print('Com notas {:.1f} e {:.1f}, a media do aluno é {:.1f}'.format(n1, n2, media))
if media >= 7:
    print('\033[32m''Aluno APROVADO')
elif 7 > media >= 5:
    print('\033[33m''Aluno de RECUPERAÇÃO')
elif media < 5:
    print('\033[31m''Aluno REPROVADO')

