def LeiaInt (msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[0:31mERRO!\033[m')
        if ok:
            break
        return  valor

n = LeiaInt('Digite um numero:')
print(format(f'voce digitou {n}'))