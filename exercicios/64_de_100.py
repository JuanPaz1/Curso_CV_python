import time
totn = 0
count = 0
c = 0
while c != 999:
    n1 = int(input('digite um numero:')) 
    if n1 != 999:
        totn += n1
        c = n1
        count+=1
    else:
        print('-------carregando-------')
        time.sleep(1)
        c = n1
print('ao todo foram {} numeros e a soma de todos é {}'.format(count, totn))
