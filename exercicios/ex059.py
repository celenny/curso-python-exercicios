n1 = float(input(('Primiro valor:')))
n2 = float(input('Segundo valor:'))
opcao = maior = 0
while opcao != 5:
    print('''   [1] somar
    [2] multiplicar
    [3] maior valor
    [4] novos numeros
    [5] sair''')
    opcao = int(input('Qual é a sua opção ?'))
    if opcao == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
           maior = n1
        else:
           maior = n2
        print('Entre {} e {} o MAIOR valor é {}'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe novos valores:')
        n1 = int(input('Primeiro valor:'))
        n2 = int(input('Segundo valor:'))
    elif opcao == 5:
        print('Foi bom enquanto durou ... Espero que tenha gostado')
    else:
        print('OPCÃO INVÁLIDA ...')
    print('=-=' * 16)
print('Fim do programa ...')
# menu de opções
