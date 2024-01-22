pt = int(input('qual o primeiro termo: '))
r = int(input('qual a razão: '))
for c in range (1, 10+1):
    print('looping {} PT ({}) + r ({})'.format(c, pt, r))
    tot = pt + r
    print('resultado: {}'.format(tot))
    pt = tot
