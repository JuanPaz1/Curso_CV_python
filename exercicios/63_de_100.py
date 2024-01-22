n = int(input('quanto numeros da sequencia você quer ver:'))
n1 = 0
n2 = 1
while n >= 0:
    print(' {} , {} '.format(n1, n2))
    n1 += n2
    n2 += n1
    n-=1
