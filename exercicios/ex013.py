sal = float(input('Qual o salario do funcionário ?R$'))
aum = sal*0.15
nsal = sal+aum
print('Um funcionario com salario de R${}, com 15% de aumento passa a receber R${:.2f}'.format(sal, nsal))
print('15% de aumento igual a R${:.2f} de acrescimo '.format(aum))
