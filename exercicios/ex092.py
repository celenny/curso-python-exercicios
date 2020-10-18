from datetime import date
dados = dict()
dados['Nome'] = str(input('Nome:'))
nasc = int(input('Ano de Nascimento:'))
dados['Idade'] = date.today().year - nasc
dados['Ctps'] = int(input('Carteira de Trabalho (0 não tem):'))
if dados['Ctps'] != 0:
    dados['Contratação'] = int(input('Ano de Contratação:'))
    dados['Salário'] = float(input('Salário:'))
    aposento = (dados['Contratação'] - nasc) + 35
    dados['Aposentadoria'] = aposento
print('-='*15)
for k, v in dados.items():
    print(f'- {k} tem valor {v}')
print('-='*15)
# dicionário aposentadoria (cadastro de trabalhador )