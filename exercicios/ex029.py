veloc = int(input('Qual a velocidade atual do carro (km/h): '))
multa = (veloc - 80)*7
if veloc <= 80:
    print('Você não ultrapassou o limete permitido , tenha um bom dia !')
else:
    print('MULTADO! você ultrapassou o limite permitido de 80 km/h  ') # radar eletronico
    print('Deverá pagar multa de R$ {:.2f}'.format(multa))
print('Dirija com segurança ...')
