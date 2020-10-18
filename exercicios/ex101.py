def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO'
    if 16 <= idade > 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'


print('-='*20)
num = int(input('Ando de nascimento:'))
print(voto(num))
print('-='*20)
# função voto
