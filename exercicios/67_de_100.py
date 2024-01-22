import time

while True:
    n1 = int(input('Digite um valor para a tabuada (ou um valor negativo para sair): '))

    if n1 < 0:
        break

    multi = 1

    while multi <= 10:
        r = n1 * multi
        print('{} x {} = {}'.format(n1, multi, r))
        multi += 1
        time.sleep(0.5)
