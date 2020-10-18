from datetime import date  # importar o ano atual da máquina
atual = date.today().year
ano = int(input('Informe o seu ano de nascimento: '))
idade = atual - ano
print('Quem nasceu em {} em {} tem {} anos '.format(ano, atual, idade))
if idade == 18:
    print('Você deve se alistar IMEDIIATAMENTE.')
elif idade < 18:
    alistamento = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento.'.format(alistamento))
    print('Seu alistameno será em {}'.format(atual + alistamento))
elif idade > 18:
    alistamento = idade - 18
    print('Você já deveria ter se alistado há {} anos'.format(alistamento))
    print('Seu alistamento foi em {}'.format(atual - alistamento))

# o programa de consulta sobre o Alistamnto militar

