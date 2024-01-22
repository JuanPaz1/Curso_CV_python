import math

l1 = int(input('qual a medida do l1: '))
l2 = int(input('qual a medida do l2: '))
hipo = l1**2 + l2**2
hipo2 = math.sqrt(hipo)

print('a hipotenusa é {:.2f}'.format(hipo2))
