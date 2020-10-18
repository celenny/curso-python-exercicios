from datetime import date
atual = date.today().year
maior = 0
menor = 0
for c in range(1, 8):
 ano = int(input('Em que ano a {}° pessoa nasceu:'.format(c)))
 idade = atual - ano
 if idade >= 18:
     maior += 1
 elif idade < 18:
     menor += 1
print('Ao todo temos {} pessoas maiores de idade'.format(maior))
print('E tambem tivemos {} pessoas menores de idade.'.format(menor))
# detector de maior e menor de idade .


