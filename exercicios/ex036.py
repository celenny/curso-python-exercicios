# Emprestimo bancário
casa = float(input('valor da casa ?R$'))
salario = float(input('Qual o seu salário ?R$'))
anos = int(input('Em quantos anos você quer quitar o emprstimo ?'))
prestação = casa/(anos * 12)
print('Você quer pagar um casa de R$ {} em {} anos'.format(casa, anos))
print('processando seus dados ...')
print('Suas prestações mensais ficaram de R$ {:.2f}'.format(prestação))
if prestação <= salario*0.3:
    print('\033[32m''Emprestimo ACEITO !')
else:
    print('\033[31m''Emprestimo NEGADO !')

