def notas(*num, sit=False):
    dado = dict()
    dado['total'] = len(num)
    dado['maior'] = max(num)
    dado['menor'] = min(num)
    dado['media'] = sum(num) / len(num)
    if sit:
        if dado['media'] >= 7:
            dado['situação'] = 'BOA'
        elif dado['media'] < 7:
            dado['situação'] = 'RUIM'
    return dado


# PROGRAMA PRINCIPAL
resp = notas(6.4, 4.3, 8.9, 7.2, sit=True)
print(resp)
# analisando notas e guardando dicionários