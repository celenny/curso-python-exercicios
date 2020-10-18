try:
    a = int(input('numerador:'))
    b = int(input('denominador:'))
    r = a / b
except (ValueError, TypeError):
    print('Tive um problema com os tipos de dados que voce digitou')
except ZeroDivisionError:
    print('Não é possivel dividir um número por zero.')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados.')
else:
    print(f'O resultado é {r:.1f}.')
finally:
    print('Obrigada ! Volte sempre.')
