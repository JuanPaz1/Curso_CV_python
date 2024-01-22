n1 = int(input('escolha um numero:'))
print('tabuada de {}'.format(n1))
for c in range(1, 10 + 1):
    print('{} * {} = {}'.format(n1, c, n1*c))
print('fim')