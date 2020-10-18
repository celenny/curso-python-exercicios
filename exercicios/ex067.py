while True:
    n = int(input('Quer ver a tabuada de qual valor ?'))
    print('-=-'*10)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{c} x {n} = {c*n}')
    print('-=-'*10)
print('PROGRAMA DE TABUADA ENCERRADO')
# tabuada versão 3.0