count = 10
pt = int(input('qual o primeiro termo: '))
r = int(input('qual a razão: '))
while count != 0:
    print('looping {} PT ({}) + r ({})'.format(count, pt, r))
    tot = pt + r
    print('resultado: {}'.format(tot))
    pt = tot
    count-=1

