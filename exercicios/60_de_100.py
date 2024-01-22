n1 = int(input('escolha um numero para ser fatorado:'))
c = n1 - 1
while c != 1:
    print('volta n: {}'.format(c))
    n1 = n1 * c
    c-=1

print('o resultado dessa fatoração é: {}'.format(n1))