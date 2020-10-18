salario = int(input('Qual o salário do funcionário: R$'))
if salario <= 1250:
    aumento = (salario*0.15) + salario
else:
    aumento = (salario*0.1) + salario
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salario, aumento))
