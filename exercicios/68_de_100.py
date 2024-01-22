import random
count = 0
while True:
    vargame = str (input('escolha [PAR] para par ou [IMP] para impar:')).upper()
    n1 = random.randint(1, 2)
    n2 = int(input('escolhar 1 ou 2:'))

    if vargame == 'IMP':
        if (n1+n2) % 2 == 1:
            print('voce ganhou')
            count+=1
        else:
            print('Você perdeu. Mais sorte na próxima!')
            break
    elif vargame == 'PAR':
        if (n1 + n2) % 2 == 0:
            print('voce ganhou')
            count += 1
        else:
            print('Você perdeu. Mais sorte na próxima!')
            break
    else:
        print('opção invalida')
print('mais sorte na proxima, você ganhou {} vezes!!!'.format(count))