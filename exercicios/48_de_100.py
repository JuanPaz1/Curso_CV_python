itot = 0
for c in range (1, 500+1):
    if c % 2 == 1 and c % 3 == 0 :
        i = c
        itot = itot + i
print('a soma de todos os impares multiplos de 3 é {}'.format(itot))
