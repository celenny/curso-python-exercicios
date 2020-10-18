print('Gerador de P.A')
print('-=-' * 7)
a1 = int(input('Primeiro termo:'))
r = int(input('Razão da P.A:'))
an = a1 + (10 - 1) * r # enésimo termo da P.A
c = a1
while c != an:
    c += r
    print('{}'.format(c), end=' → ')
print('FIM')
# P.A versão 2.0
