mil = 0
totgast = 0
minprot = 0
protmin = 'na'
while True:
    prot=str(input('qual o produlto que esta comprando?'))
    rs=float(input('qual o seu preço?'))
    totgast+=rs
    if rs > 1000:
        mil+=1
    if minprot != 0 or rs<minprot:
        protmin = prot
        minprot = rs
    count=str(input('quer continuar [N/S]')).upper()
    if count == 'N':
        break
print('o total gasto foi {} \n{} produltos custavam mais de 1000 reais\no produlto mais barato foi {}'.format(totgast, mil, protmin))