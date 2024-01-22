agemasc = 0
agetot = 0
cfem = 0
count = 0
for c in range (0, 4):
    nome = str(input('qual o seu nome?'))
    age = int(input('qual sua idade?'))
    sexo = str(input('M ou F?')).upper()
    if sexo == 'M' and age >= agemasc :
        masc = nome
    if sexo == 'F' and age <= 20 :
        cfem = cfem + 1
    agetot = agetot + age
    count = count + 1
print('a idade media das pessoas é {}, o homem mais velho é o {} e {} mulher tem menos de 20 anos'.format(agetot/count,masc, cfem  ))
