sx = str('?').upper()
while sx !='M' and sx !='F':
    s = str(input('digite seu sexo [F] para Feminino ou [M] para masculino:')).upper()
    sx = s
    print('sexo invalido seu animal')
if sx == 'M':
    print('olá caro amigo')
else:
    print('olá cara amiga')
