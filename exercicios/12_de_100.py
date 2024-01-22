n1=float(input('qual o valor do produlto: '))
n2=float(input('digite de quanto é o cupom de desconto em %: '))
desc = n2/100
n3 = n1*desc
print('o seu produto que custa {} com {} % de desconto fica {}'.format(n1, n2, n1-n3))
