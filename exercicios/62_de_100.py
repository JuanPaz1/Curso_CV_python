pt = int(input('qual o primeiro termo: '))
r = int(input('qual a razão: '))
for c in range (1, 10+1):
    print('looping {} PT ({}) + r ({})'.format(c, pt, r))
    tot = pt + r
    print('resultado: {}'.format(tot))
    pt = tot
count = int(input('voce que ver mais quantos termos?'))
while count != 0:
    print('looping {} PT ({}) + r ({})'.format(c, pt, r))
    tot = pt + r
    print('resultado: {}'.format(tot))
    pt = tot
    count-=1
    if count <= 1:
        c2 = int(input('voce quer ver mais quantos termos?'))
        count = c2

