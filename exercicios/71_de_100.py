valor=int(input('quanto voce quer sacar?'))
total = valor
ced50 = 50
totced = 0
while True:
    if total >= ced50:
        total -= ced50
        totced += 1
    else:
        print('o total de {} cedulas de R$ {}'.format(totced, ced50))
        if ced50 == 50:
            ced50 = 20
        elif ced50 == 20:
            ced50 = 10
        elif ced50 == 20:
            ced50 = 1
        totced = 0
        if total == 0:
            break