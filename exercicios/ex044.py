valor = float(input('Preçe das compras : R$'))
print(' FORMAS DE PAGAMENTO: ')
print('[ 1 ] à vista (dinheiro/cheque)')
print('[ 2 ] à vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção ?'))
if opcao == 1:
    total = valor - (valor * 0.1)
    print('Parabens! por comprar à vista voce acabar de ganhar um desconto de 10% ')
elif opcao == 2:
    total = valor - (valor * 0.05)
    print('Muito obrigada! por comprar à vista no cartão você ganha 5% de desconto ')
elif opcao == 3:
    total = valor
    parcela = valor/2
    print('Sua compra será parcelada em 2x SEM juros de {:.2f}'.format(parcela))
elif opcao == 4:
    total = valor + (valor * 0.2)
    totparc =int(input('Em quantas parcelas ?'))
    parcel = total/totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM juros de 20%'.format(totparc, parcel))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))


