
n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))

rs = n1 + n2
rm = n1 - n2
rdiv = n1 / n2
rmult = n1 * n2
rpot = n1 ** n2
rsdiv = n1 // n2
rrestdiv = n1 % n2

print('a soma entre {} e {} é igual a {}'.format(n1, n2, rs))
print('a subtração entre {} e {} é igual a {}'.format(n1, n2, rm))
print('a multiplicação entre {} e {} é igual a {}'.format(n1, n2, rmult))
print('a divisão entre {} e {} é igual a {}'.format(n1, n2, rdiv))
print('a potencia de {} por {} é igual a {}'.format(n1, n2, rpot))
print('a divisao real {} e {} é igual a {}'.format(n1, n2, rsdiv))
print('o resto da divisão entre {} e {} é igual a {}'.format(n1, n2, rrestdiv))
