min = 0.0
max = 0.0

for c in range(1, 5 + 1):
    kg = float(input('qual o seu peso?'))
    if min == 0 or kg < min :
        min = kg
    if kg >= max or max == 0 :
        max = kg
print('o menor peso foi {:.1f} e o maior foi {:.1f}'.format(min, max))
