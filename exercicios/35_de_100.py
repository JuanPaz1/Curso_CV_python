r1 = int(input('qual o comprimento da reta1'))
r2 = int(input('qual o comprimento da reta2'))
r3 = int(input('qual o comprimento da reta3'))

if r1 < r2 + r3 and r2 < r3 + r3 and r3< r1 + r2:
    print('forma triangulo')
else:
    print('nao forma triangulo')