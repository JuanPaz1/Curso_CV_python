c = 0
totn = 0
while True:
    n = int(input('digite um numero (digite 999 para parar):'))
    if n == 999:
        break
    else:
        totn +=n
        c+= 1
print('ao todo foram {} numero e a sua soma é igual a {}'.format(c, totn))