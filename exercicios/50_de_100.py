par = 0
for c in range(0, 6):
    n1 = int(input('escolha um numero entre 1 e 6:'))
    if 0 <= n1 >= 7 :
        print('numero invalido, tente novamente')
        break
    else:
        if n1 % 2 == 0:
            par = par + n1
print('o total da soma de numeros pares é {}'.format(par))
