n1 = str(input('digite um numero de 0 a 9999: '))

n = int (n1)
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print('o numero digitado foi {}'.format(n))
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('centena {}'.format(c))
print('milhar {}'.format(m))

