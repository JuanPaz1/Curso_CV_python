n1 = float(input('qual o valor da primeira nota?'))
n2 = float(input('qual o valor da segunda nota?'))

m = (n1 + n2 ) /2

if m < 5 :
    print('Reprovado')
elif m >= 5 and m < 7 :
    print('recuperação')
elif m >= 7 :
    print(' aprovado ')
