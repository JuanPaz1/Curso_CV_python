c = 'S'
m = 0
ntot = 0
maxnum = 0
minnum = 0
while c != 'N':
    n = int(input('digite um numero:'))
    m+=1
    ntot+=n
    if maxnum == 0 or maxnum > n:
        maxnum = n

    if minnum == 0 or minnum < n:
        minnum = n

    c = str(input('você quer continuar?')).upper()
print('a media entre os numero é {}\no maior numero foi {}\no menor foi {}'.format(ntot/m, maxnum, minnum))