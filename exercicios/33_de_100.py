n1 = int(input('digite o primeiro numero:'))
n2 = int(input('digite o segundo numero:'))
n3 = int(input('digite o terceiro numero: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3< n1 and n3<n2:
    menor = n3

maior = n1
if n2>n3 and n2>n1:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
