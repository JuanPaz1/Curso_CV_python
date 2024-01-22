numeros = list()
vpar = list()
vimp = list ()
for c in range (0, 7):
    valor = int(input('digite um valor:'))
    if valor%2 == 0:
        vpar.append(valor)
    else:
        vimp.append(valor)
    vpar.sort()
    vimp.sort()
    numeros.append(vpar[:])
    numeros.append(vimp[:])
print(numeros)
print(vpar)
print(vimp)