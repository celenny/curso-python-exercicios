print('OS 10 primeiros termos da P.A :')
print('=-'*18)
a1 = int(input('Primeiro termo:'))
r = int(input('Razão:'))
an = a1 + (10 - 1)*r  # enésimo termo da P.A
for c in range(a1, an + r, r):
    print('{}'.format(c), end='→ ')
print('FIM!')
print('-='*18)
# P.A versão 1.0
