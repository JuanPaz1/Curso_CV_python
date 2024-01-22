import random

n = random.uniform(0 , 5).__trunc__()

nj = int(input('escolha um numero entra 0 e 5:'))

if n == nj:
    print('parabens voce acertou, eu pensei em {} e vc pediu {}'.format(n, nj))
else:
    print('infelizmente voce errou eu pensei em {} e voce disse {}'.format(n, nj))
