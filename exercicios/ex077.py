grlpwr = ('poder', 'mulheres', 'programar', 'pyladies',
            'amor', 'ciência', 'computação', 'tecnologia',
          'ação', 'presença', 'união', 'empoderamento', 'futuro')
for palavra in grlpwr:
    print(f'\nA palavra {palavra.upper()} temos ', end='')
    for letra in palavra:
        if letra.lower() in 'aáãeéêiou':
            print(letra, end=' ')


