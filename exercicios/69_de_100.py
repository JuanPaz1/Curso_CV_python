totage = 0
totsxm = 0
totsxf = 0
while True:
    age = int (input('qual a sua idade?'))
    sx = str (input('qual o seu sexo?[M/F]')).upper()
    if age >= 18:
      totage+=1
    if sx == 'M':
        totsxm+=1
    if sx == 'F' and age < 20:
        totsxf+=1
    resp = str(input('você quer continuar? [s/n]')).upper()
    if resp == 'N':
        break
    elif resp != 'S':
        print('Resposta inválida. Encerrando o programa.')
        break
print('tivemos {} maiores de idade cadastradas \n {} homens cadastrados \n {} mulheres com menos de 20 cadastradas'.format(totage, totsxm, totsxf))