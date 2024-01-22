from time import sleep
print('contagem regresiva de fogos:')
for c in range(10, -1, -1):
    print('{}...'.format(c))
    sleep(0.5)
print('FOGOS ESTOURANDO!!!')