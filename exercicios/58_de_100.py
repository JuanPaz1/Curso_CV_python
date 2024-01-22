import random
import time
c = 1
p = 0
count = 0
while c != p:
    c = random.randint(0, 10)
    count+=1
    p = int(input('escolha um numero:'))
    print('tente novamente maquina jogou {} e voce {}'.format(c, p))
print('voce ganhou, foram apenas {} tentativas'.format(count))