n1 = int(input('qual o numero que vai ser verificado?'))

if n1 > 1:
    for c in range(2, n1):
            if(n1 % c) == 0:
                print('não é primo')
                break
            else:
                print('é primo')
else:
    print('não é primo')