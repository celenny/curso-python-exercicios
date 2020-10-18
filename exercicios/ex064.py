soma = quant = 0
num = int(input('Digite um valor [999 para parar]:'))
while num != 999:
    soma += num
    quant += 1
    num = int(input('Digite um valor [999 para parar]:'))
print(f'Você digitou {quant} números e a soma entre eles foi {soma}')
# tratando válores versão 1.0
'''Execução de comandos tipo FLAG no caso do exemplo o número 999
 é o ponto de parada ou seja nossa FLAG'''

