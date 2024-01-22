c = 0
while c != 5:
    print('======Calculadora======')
    n1=int(input('digite um numero:'))
    n2=int(input('digite outro numero:'))
    op=int(input('escolha a operação \n[1] para somar\n[2]para multiplicar\n[3]qual o maior?\n[4] novos numeros\n[5]sair do programa'))
    if op == 1:
        r = n1 + n2
        print('o resultado da soma entre {} e {} é {}'.format(n1, n2, r))
    elif op == 2:
        r = n1 * n2
        print('o resultado da multiplicação entre {} e {} é {}'.format(n1, n2, r))
    elif op == 3:
        if n1 > n2:
            print('o maior é {}'.format(n1))
        elif n2 > n1:
            print('o maior é {}'.format(n2))
        else:
            print('eles são iguais')
    elif op == 4:
        c = op
    elif op == 5:
        c = op
    else:
        print('valor invalido')

