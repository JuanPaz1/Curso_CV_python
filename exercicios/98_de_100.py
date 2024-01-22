import time


def contador(a, b, c):
    print(f'Contagem de 1 a 10:')

    for i in range(0, 10 + 1):
        print(i, end=' ')
        time.sleep(0.5)

    print('\nContagem regressiva de 10 a 1:')
    for i in range(10, 0, -1):
        print(i, end=' ')
        time.sleep(0.5)

    print(f'\nContagem de {a} a {b} com passo {c}:')
    for i in range(a, b + 1, c):
        print(i, end=' ')
        time.sleep(0.5)


print('FUNÇÃO CONTADOR:')
ini = int(input('INICIO:'))
fim = int(input('FIM:'))
passo = int(input('PASSO:'))
contador(ini, fim, passo)
