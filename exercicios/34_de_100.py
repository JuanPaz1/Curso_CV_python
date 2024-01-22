sl = float(input('qual o seu salario?'))

if sl <= 1250.00:
    print('seu novo salario é: {:.2f}'.format((sl *(15/100)) + sl ))
else:
    print('seu novo salario é de {:.2f}'.format((sl * (10/100)) + sl))
